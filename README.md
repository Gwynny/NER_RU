# NER_RU

NER-Модель для извлечения адресов, ФИО и ИНН (Зад 1 и 2)
Была выбрана библиотека Natasha. Выбор был между Natasha, DeepPavlov и Spacy
Эта статья помогла в выборе https://natasha.github.io/ner/
TLDR: Наташа компактнее DP и быстрее, качество чуть-чуть похуже

## Example

Посмотреть, как работает модель, необходимо запустить encode.py на своих данных или на тестовых. P.S. encode принтит результат модели и сохраняет его в output/encoded.txt
```
usage: encode.py [-h] [--text-path <str>]

optional arguments:
  -h, --help            show this help message and exit
  --text-path <str>, -p <str>
                        path to your test txt file
```

Расшифровка с помощью decode.py сохранненого в output/encoded.txt txt файл 
