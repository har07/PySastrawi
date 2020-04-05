Sastrawi Python
===============

Sastrawi Python is a simple python library which allows you to reduce inflected words in Indonesian Language (Bahasa Indonesia) to their base form ([stem](http://en.wikipedia.org/wiki/Stemming)). This is Python port of the original [Sastrawi](https://github.com/sastrawi/sastrawi) project written in PHP (credits goes to the original author and contributors of Sastrawi PHP).

Version 2.0 contains heavy refactoring of the codebase to be simpler and more pythonic, credits to [@kekavigi](https://github.com/kekavigi) and other contributors.


[![Build Status](https://travis-ci.org/har07/PySastrawi.svg?branch=master)](https://travis-ci.org/har07/PySastrawi)
[![Coverage Status](https://coveralls.io/repos/github/har07/PySastrawi/badge.svg?branch=master)](https://coveralls.io/github/har07/PySastrawi?branch=master)
[![PyPI version](https://badge.fury.io/py/PySastrawi.svg)](https://badge.fury.io/py/PySastrawi)

Read this in [Bahasa Indonesia](README.id.md)

Installation
-------------

Install Sastrawi using [pip](https://docs.python.org/3.6/installing/index.html): `pip install PySastrawi`

Example usage
-----------

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

License
--------

Sastrawi Python registered under MIT License (MIT).

This project contains dictionary of Indonesian words from Kateglo with [CC-BY-NC-SA 3.0](http://creativecommons.org/licenses/by-nc-sa/3.0/) license.

More Information
----------------------

- [Sastrawi PHP Repository page](https://github.com/sastrawi/sastrawi)
