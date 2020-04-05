# Stemmer

Ini adalah kode Python sederhana yang memungkinkan anda untuk mengubah kata berimbuhan dalam Bahasa Indonesia ke bentuk kata dasar ([stem](http://en.wikipedia.org/wiki/Stemming)). Proyek ini adalah perbaikan dari proyek [PySastrawi]https://github.com/har07/PySastrawi).

Penggunaan
-----------

```python
import sastrawi

stemmer = sastrawi.Stemmer()

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
res = stemmer.context('meniru-nirukannya'))
# ['tiru', [('me', 'DP'), ('nya', 'PP'), ('kan', 'DS')]]

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
