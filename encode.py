import argparse
import json
from app.api.src.extractor import Extractor

parser = argparse.ArgumentParser()
parser.add_argument("--text-path", "-p", default='data/test.txt',
                    dest="text_path", type=str, metavar='<str>',
                    help="path to test txt file")
args = parser.parse_args()

d = {}
mod_text = []
ner_proccessor = Extractor(d)

with open(args.text_path, 'r', encoding='utf-8') as reader, open('output/encoded.txt', 'w') as writer:
    lines = reader.readlines()
    for line in lines:
        line = ner_proccessor.ner_inference(line)
        print(f'После кодировки: {line}')
        writer.write(line)

hashed_dict = ner_proccessor.dict_with_hashes
with open('output/hashed_dict.json', 'w') as file:
    json.dump(hashed_dict, file)

