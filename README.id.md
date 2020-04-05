PySastrawi
===============

Sastrawi Python adalah library python sederhana untuk mengubah kata-kata berimbuhan dalam Bahasa Indonsia kembali ke bentuk kata dasarnya, atau yang dikenal dengan istilah [*stemming*](http://en.wikipedia.org/wiki/Stemming).
Repository ini adalah hasil *porting* dari [Sastrawi](https://github.com/sastrawi/sastrawi), library dengan fungsi yang sama untuk bahasa pemrograman PHP.
Di PySastrawi versi 2.0 source code PySastrawi mengalami refactoring agar menjadi lebih simpel dan mengikuti style coding python standar, credits to [@kekavigi](https://github.com/kekavigi) dan kontributor lainnya (lihat daftar kontributor selengkapnya [di sini](https://github.com/har07/PySastrawi/graphs/contributors)).

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
import sastrawi

stemmer = sastrawi.Stemmer()

# stemming process
sentence = 'Perekonomian Indonesia sedang dalam pertumbuhan yang membanggakan'
output   = stemmer.stem(sentence)

print(output)
# ekonomi indonesia sedang dalam tumbuh yang bangga

print(stemmer.stem('Mereka meniru-nirukannya'))
# mereka tiru
```

Demo (version 1.2.0)
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
