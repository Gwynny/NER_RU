import argparse
import json
from src.extractor import Extractor

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
        line = ner_proccessor.replace_inn(line)
        line = ner_proccessor.replace_ner(line, 'addr')
        line = ner_proccessor.replace_ner(line, 'fio')
        print(line)
        writer.write(line)

hashed_dict = ner_proccessor.dict_with_hashes
with open('output/hashed_dict.json', 'w') as file:
    json.dump(hashed_dict, file)

