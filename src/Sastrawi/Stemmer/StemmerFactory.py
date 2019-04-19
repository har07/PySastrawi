import os
from cachetools import cached, LRUCache
from Sastrawi.Dictionary.ArrayDictionary import ArrayDictionary
from Sastrawi.Stemmer.Stemmer import Stemmer

class StemmerFactory(object):
    """ Stemmer factory helps creating pre-configured stemmer """

    def create_stemmer(self, isDev=False):
        """ Returns Stemmer instance """
        if isDev:
            words = self.get_words_from_file()
            dictionary = ArrayDictionary(words)
        else:
            dictionary = self.get_prod_words_dictionary()

        stemmer = Stemmer(dictionary)

        return stemmer

    @cached(cache=LRUCache(maxsize=32))
    def get_prod_words_dictionary(self):
        words = self.get_words_from_file()
        dictionary = ArrayDictionary(words)
        return dictionary

    def get_words_from_file(self):
        current_dir = os.path.dirname(os.path.realpath(__file__))
        dictionaryFile = current_dir + '/data/kata-dasar.txt'

        if not os.path.isfile(dictionaryFile):
            raise RuntimeError('Dictionary file is missing. It seems that your installation is corrupted.')

        text = ''
        with open(dictionaryFile, 'r') as f:
            text = f.read()
        return text.split('\n')