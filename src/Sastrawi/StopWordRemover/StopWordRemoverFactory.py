import os
from cachetools import cached, LRUCache
from Sastrawi.Dictionary.ArrayDictionary import ArrayDictionary
from Sastrawi.StopWordRemover.StopWordRemover import StopWordRemover

class StopWordRemoverFactory(object):
    """description of class"""

    def create_stop_word_remover(self, isDev=False):
        if isDev:
            stopWords = self.get_stop_words()
            dictionary = ArrayDictionary(stopWords)
        else:
            dictionary = self.get_prod_stop_word_dictionary()

        stopWordRemover = StopWordRemover(dictionary)
        return stopWordRemover

    @cached(cache=LRUCache(maxsize=8))
    def get_prod_stop_word_dictionary(self):
        stopWords = self.get_stop_words()
        return ArrayDictionary(stopWords)

    def get_stop_words(self):
        current_dir = os.path.dirname(os.path.realpath(__file__))
        dictionaryFile = current_dir + '/data/stopword_tala_2003.txt'

        if not os.path.isfile(dictionaryFile):
            raise RuntimeError('Stopword file is missing. It seems that your installation is corrupted.')

        text = ''
        with open(dictionaryFile, 'r') as f:
            text = f.read()
        return text.split('\n')