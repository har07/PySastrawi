Sastrawi Python
===============

Sastrawi Python is a simple python library which allows you to reduce inflected words in Indonesian Language (Bahasa Indonesia) to their base form ([stem](http://en.wikipedia.org/wiki/Stemming)).
This is Python port of the original [Sastrawi](https://github.com/sastrawi/sastrawi) project written in PHP (credits goes to the original author and contributors of Sastrawi PHP).


[![Build Status](https://travis-ci.org/har07/PySastrawi.svg?branch=master)](https://travis-ci.org/har07/PySastrawi)
[![Coverage Status](https://coveralls.io/repos/github/har07/PySastrawi/badge.svg?branch=master)](https://coveralls.io/github/har07/PySastrawi?branch=master)
[![PyPI version](https://badge.fury.io/py/PySastrawi.svg)](https://badge.fury.io/py/PySastrawi)

Cara Install
-------------

Sastrawi dapat di-*install* menggunakan [pip](https://docs.python.org/3.6/installing/index.html), dengan menjalankan perintah berikut di terminal/command prompt : `pip install PySastrawi`

Penggunaan
-----------

Jalankan baris-baris kode berikut di *Python interactive terminal* :

```python
# import StemmerFactory class
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory

# create stemmer
factory = StemmerFactory()
stemmer = factory.create_stemmer()

# stemming process
sentence = 'Perekonomian Indonesia sedang dalam pertumbuhan yang membanggakan'
output   = stemmer.stem(sentence)

print(output)
# ekonomi indonesia sedang dalam tumbuh yang bangga

print(stemmer.stem('Mereka meniru-nirukannya'))
# mereka tiru
```

Demo
--------

Live demo URL : https://pysastrawi-demo.appspot.com/

Repository : https://github.com/har07/pystastrawi-demo

Lisensi
--------

Lisensi Sastrawi Python adalah MIT License (MIT).

Project ini mengandung kamus kata dasar yang berasal dari Kateglo dengan lisensi [CC-BY-NC-SA 3.0](http://creativecommons.org/licenses/by-nc-sa/3.0/).

Informasi Lebih Lanjut
----------------------

- [Sastrawi PHP Repository page](https://github.com/sastrawi/sastrawi)
