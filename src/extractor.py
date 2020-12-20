import hashlib
import re
from natasha import NamesExtractor, AddrExtractor, MorphVocab
from src.utils import check_inn


class Extractor:
    """
        NER-Модель для извлечения адресов, ФИО и ИНН
        Была выбрана библиотека Natasha. Выбор был между Natasha, DeepPavlov и Spacy
        Эта статья помогла в выборе https://natasha.github.io/ner/
        TLDR: Наташа компактнее DP и быстрее, качество чуть-чуть похуже
    """

    def __init__(self, dict_with_hashes: dict):
        """
        Initializing the model
        :param dict_with_hashes: dict to store encoded information
        """
        self.dict_with_hashes = dict_with_hashes
        vocab = MorphVocab()
        self.addr_extractor = AddrExtractor(vocab)
        self.name_extractor = NamesExtractor(vocab)

    def replace_ner(self, line, ner_type):
        """
            Replacing Names or Addresses
        """
        assert ner_type in {'fio', 'addr'}
        assert type(line) == str

        detected_ners = []
        if ner_type == 'fio':
            for item in list(self.name_extractor(line)):
                if (item.fact.first is not None) and (item.fact.last is not None) and (item.fact.middle is not None):
                    detected_ners.append(line[item.start:item.stop])
        elif ner_type == 'addr':
            for addr_match in list(self.addr_extractor(line)):
                address = line[addr_match.start:addr_match.stop]
                detected_ners.append(address)

        for ner in detected_ners:
            hashed_name = hashlib.md5(ner.encode()).hexdigest()
            self.dict_with_hashes[hashed_name] = ner
            line = line.replace(ner, " " + hashed_name + " ")

        return line

    def replace_inn(self, line):
        """
            Replacing INN
        """
        inns = re.findall(r'\b\d{12}\b', line)
        if not inns:
            return line

        for inn in inns:
            if check_inn(inn):
                hashed_inn = hashlib.md5(inn.encode()).hexdigest()
                self.dict_with_hashes[hashed_inn] = inn
                line = line.replace(inn, hashed_inn)
            else:
                line = line.replace(inn, 'НЕКОРРЕКТНЫЙ_ИНН')
        return line
