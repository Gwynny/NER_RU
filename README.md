# NER_RU

Что нового?
- Переделал на Async API. АПИ Работает, но докер у меня на машине не робит, а разбираться в выходные не хочется (Hyper-V не робит)
- Словарь с зашифрованными данными хранится на серве. После каждого запроса на зашифровку обновляется (наверно не супер - приходится открывать файл и обновлять его). 
- Изменена структура экстактора NER, теперь pipeline с процессингом и заменой ner лежит внутри, а не снаружи (раньше был в encode.py и decode.py).
- Теперь некоррентные ИНН тоже шифруются и дешифруются. FYI данный код работает только для физ лиц (12 чисел ИНН).

## Test
Encoding

![Работа АПИ. Encoding](https://drive.google.com/file/d/1Lc2jmStfle3w3a7wvnnXIy-xS8Br5-dZ/view?usp=sharing)

Decoding

![Работа АПИ. Decoding](https://drive.google.com/file/d/1lPxryGMrMhhqPt0FHYJCTeB54nXqoQ7v/view?usp=sharing)
