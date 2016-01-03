import os
from Dictionary.ArrayDictionary import ArrayDictionary
from Stemmer import Stemmer
from CachedStemmer import CachedStemmer
from Cache.ArrayCache import ArrayCache

""" Stemmer factory helps creating pre-configured stemmer """
class StemmerFactory(object):
    APC_KEY = 'sastrawi_cache_dictionary'

    def createStemmer(self, isDev=False):
        """ Returns Stemmer instance """

        words = self.getWords()
        dictionary = ArrayDictionary(words)
        stemmer = Stemmer(dictionary)

        resultCache = ArrayCache()
        cachedStemmer = CachedStemmer(resultCache, stemmer)

        return cachedStemmer

    def getWords(self, isDev=False):
        if isDev or callable(getattr(self, 'apc_fetch')):
            words = self.getWordsFromFile()
        else:
            words = apc_fetch(self.APC_KEY)
            if not words:
                words = self.getWordsFromFile()
                apc_store(self.APC_KEY, words)

    def getWordsFromFile(self):
        current_dir = os.path.dirname(os.path.realpath(__file__))
        dictionaryFile = current_dir + '/../../../data/kata-dasar.txt'
        if not os.path.isfile(dictionaryFile):
            raise RuntimeError('Dictionary file is missing. It seems that your installation is corrupted.')

        dictionaryContent = ''
        with open(dictionaryFile, 'r') as f:
            dictionaryContent = f.read()

        return dictionaryContent.split('\n')