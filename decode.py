import json

with open('output/hashed_dict.json', 'r') as file:
    hashed_dict = json.load(file)

mod_text = []
with open('output/encoded.txt', 'r') as reader:
    lines = reader.readlines()
    for line in lines:
        decoded_line = []
        for word in line.split():
            if word in hashed_dict.keys():
                decoded_line.append(hashed_dict[word])
            else:
                decoded_line.append(word)
        print(' '.join(decoded_line))