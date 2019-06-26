# PySastrawi

[![Build Status](https://travis-ci.org/kekavigi/PySastrawi.svg?branch=master)](https://travis-ci.org/kekavigi/PySastrawi)
[![Coverage Status](https://coveralls.io/repos/github/kekavigi/PySastrawi/badge.svg)](https://coveralls.io/github/kekavigi/PySastrawi)

## English

PySastrawi is a simple Python package which allows you to reduce inflected words in Indonesian Language (Bahasa Indonesia) to their base form ([stem](http://en.wikipedia.org/wiki/Stemming)). This is Python port of the original [Sastrawi](https://github.com/sastrawi/sastrawi) project written in PHP (credits goes to the original author and contributors of Sastrawi PHP).

Installation
------------
PySastrawi can be installed using [pip](https://docs.python.org/3.6/installing/index.html), by running `pip install PySastrawi` in terminal/command prompt.

Usage
------

```python
import Sastrawi

stemmer = Stemmer()

sentences = ['Perekonomian Indonesia sedang dalam pertumbuhan yang membanggakan',
             'Mereka meniru-nirukannya']

# stemming process
for sentence in sentences:
    print(stemmer.stem(sentence))
# ekonomi indonesia sedang dalam tumbuh yang bangga
# mereka tiru

# remove stopwords
for sentence in sentences:
    print(stemmer.stem(sentence))
# perekonomian indonesia pertumbuhan membanggakan
# meniru-nirukannya

# more about stemming process
res = stemmer.context('kemerdekaannya')

print(res.result)
# ('merdeka', [('nya', 'PP'), ('an', 'DS'), ('ke', 'DP')])

```

Demo
--------

Live demo URL : https://pysastrawi-demo.appspot.com/
Repository : https://github.com/har07/pystastrawi-demo

License
--------

Sastrawi is based on MIT License (MIT).

This project also contains list of Indonesian stem words created by Kateglo
with [CC-BY-NC-SA 3.0](http://creativecommons.org/licenses/by-nc-sa/3.0/) license.

More information
----------------------

- [Sastrawi PHP Repository page](https://github.com/sastrawi/sastrawi)


## Indonesia

PySastrawi adalah package Python sederhana yang memungkinkan anda untuk mengubah kata berimbuhan dalam Bahasa Indonesia ke bentuk kata dasar ([stem](http://en.wikipedia.org/wiki/Stemming)). Proyek ini adalah port dari proyek [Sastrawi](https://github.com/sastrawi/sastrawi) yang ditulis dalam PHP (kredit untuk pencipta dan semua kontributor Sastrawi PHP)

Cara Install
-------------

PySastrawi dapat di-*install* menggunakan [pip](https://docs.python.org/3.6/installing/index.html), dengan menjalankan perintah `pip install PySastrawi` di terminal/command prompt.

Penggunaan
-----------

```python
import Sastrawi

stemmer = Stemmer()

sentences = ['Perekonomian Indonesia sedang dalam pertumbuhan yang membanggakan',
             'Mereka meniru-nirukannya']

# proses stemming
for sentence in sentences:
    print(stemmer.stem(sentence))
# ekonomi indonesia sedang dalam tumbuh yang bangga
# mereka tiru

# hilangkan stopwords
for sentence in sentences:
    print(stemmer.stem(sentence))
# perekonomian indonesia pertumbuhan membanggakan
# meniru-nirukannya

# lebih dalam tentang proses stemming
res = stemmer.context('kemerdekaannya')

print(res.result)
# ('merdeka', [('nya', 'PP'), ('an', 'DS'), ('ke', 'DP')])
```

Demo
--------

Live demo URL : https://pysastrawi-demo.appspot.com/
Repository : https://github.com/har07/pystastrawi-demo

Lisensi
--------

Lisensi PySastrawi adalah MIT License (MIT).

Project ini mengandung kamus kata dasar yang berasal dari Kateglo dengan lisensi
[CC-BY-NC-SA 3.0](http://creativecommons.org/licenses/by-nc-sa/3.0/).

Informasi Lebih Lanjut
----------------------

- [Halaman Repository Sastrawi PHP](https://github.com/sastrawi/sastrawi)
