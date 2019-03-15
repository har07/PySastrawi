import os
from cachetools import cached, LRUCache
from Sastrawi.Dictionary.ArrayDictionary import ArrayDictionary
from Sastrawi.Stemmer.Stemmer import Stemmer
from Sastrawi.Stemmer.CachedStemmer import CachedStemmer
from Sastrawi.Stemmer.Cache.ArrayCache import ArrayCache

class StemmerFactory(object):
    """ Stemmer factory helps creating pre-configured stemmer """
    #APC_KEY = 'sastrawi_cache_dictionary'

    def create_stemmer(self, isDev=False):
        """ Returns Stemmer instance """
        if isDev:
            words = self.get_words_from_file()
            dictionary = ArrayDictionary(words)
        else:
            dictionary = self.get_prod_words_dictionary()

        stemmer = Stemmer(dictionary)

        resultCache = ArrayCache()
        cachedStemmer = CachedStemmer(resultCache, stemmer)

        return cachedStemmer

    @cached(cache=LRUCache(maxsize=32))
    def get_prod_words_dictionary(self):
        words = self.get_words_from_file()
        dictionary = ArrayDictionary(words)
        return dictionary

    #def get_words(self, isDev=False):
        #if isDev or callable(getattr(self, 'apc_fetch')):
        #    words = self.getWordsFromFile()
        #else:
        #    words = apc_fetch(self.APC_KEY)
        #    if not words:
        #        words = self.getWordsFromFile()
        #        apc_store(self.APC_KEY, words)
    #    return self.get_words_from_file()

    def get_words_from_file(self):
        current_dir = os.path.dirname(os.path.realpath(__file__))
        dictionaryFile = current_dir + '/data/kata-dasar.txt'

        if not os.path.isfile(dictionaryFile):
            raise RuntimeError('Dictionary file is missing. It seems that your installation is corrupted.')

        text = ''
        with open(dictionaryFile, 'r') as f:
            text = f.read()
        return text.split('\n')