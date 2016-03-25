Sastrawi
========

| Sastrawi is a simple Python library which allows you to reduce
  inflected words in Indonesian Language (Bahasa Indonesia) to their
  base form (`stem`_).
| This is Python port of the original `Sastrawi`_ project written in
  PHP.

|Build Status|
|Coverage Status|

Installation
------------

Sastrawi can be installed via `pip`_, by running the following commands
in terminal/command prompt : ``pip install Sastrawi``

Example Usage
-------------

Run the following commands in *Python interactive terminal* :

.. code:: python

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

Demo
---------

Live demo : https://pysastrawi-demo.appspot.com/

Repository : https://github.com/har07/pystastrawi-demo

More Info
---------

-  `Sastrawi PHP Repository page`_

.. _stem: http://en.wikipedia.org/wiki/Stemming
.. _Sastrawi: https://github.com/sastrawi/sastrawi
.. _pip: https://docs.python.org/3.6/installing/index.html
.. _Sastrawi PHP Repository page: https://github.com/sastrawi/sastrawi

.. |Build Status| image:: https://travis-ci.org/har07/PySastrawi.svg?branch=master
   :target: https://travis-ci.org/har07/PySastrawi
.. |Coverage Status| image:: https://coveralls.io/repos/har07/sastrawi/badge.svg?branch=master&service=github
   :target: https://coveralls.io/github/har07/sastrawi?branch=master
