import json
from fastapi import APIRouter

from api.model import Input, Output
from api.src.extractor import Extractor

ner = APIRouter()
ner_proccessor = Extractor()


# Path for named entity recognition service
@ner.post("/encode", response_model=Output)
async def named_entity_recognition(item: Input):
    text = item.text
    result = ner_proccessor.ner_inference(text)
    return {"entities": result}


@ner.post("/decode", response_model=Output)
async def named_entity_recognition(item: Input):
    with open("./api/data/dict.json", 'r') as file:
        hashed_dict = json.load(file)

    text = item.text
    decoded_line = []
    for word in text.split():
        if word in hashed_dict.keys():
            decoded_line.append(hashed_dict[word])
        else:
            decoded_line.append(word)

    return {"entities": ' '.join(decoded_line)}
