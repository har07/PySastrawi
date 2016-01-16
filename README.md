Sastrawi
=========

Sastrawi is a simple Python library which allows you to reduce inflected words in Indonesian Language (Bahasa Indonesia) to their base form ([stem](http://en.wikipedia.org/wiki/Stemming)).
This is Python port of the original [Sastrawi](https://github.com/sastrawi/sastrawi) project written in PHP.


[![Build Status](https://travis-ci.org/har07/sastrawi.svg?branch=master)](https://travis-ci.org/har07/sastrawi)
[![Coverage Status](https://coveralls.io/repos/har07/sastrawi/badge.svg?branch=master&service=github)](https://coveralls.io/github/har07/sastrawi?branch=master)

Cara Install
-------------

Sastrawi dapat di*install* menggunakan [pip](https://docs.python.org/3.6/installing/index.html), dengan menjalankan perintah berikut di terminal/command prompt : `pip install Sastrawi`

Penggunaan
-----------

Jalankan baris-baris kode berikut di *Python interactive terminal* :

```python
# import Sastrawi package
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory

# create stemmer
factory = StemmerFactory()
stemmer = factory.create_stemmer()

# stem
sentence = 'Perekonomian Indonesia sedang dalam pertumbuhan yang membanggakan'
output   = stemmer.stem(sentence)

print(output)
# ekonomi indonesia sedang dalam tumbuh yang bangga

print(stemmer.stem('Mereka meniru-nirukannya'))
# mereka tiru
```

Informasi Lebih Lanjut
----------------------

- [Sastrawi PHP Repository page](https://github.com/sastrawi/sastrawi)