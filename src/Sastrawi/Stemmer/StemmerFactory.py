import os
from Sastrawi.Dictionary.ArrayDictionary import ArrayDictionary
from Sastrawi.Stemmer.Stemmer import Stemmer
from Sastrawi.Stemmer.CachedStemmer import CachedStemmer
from Sastrawi.Stemmer.Cache.ArrayCache import ArrayCache

class StemmerFactory:
    """ Stemmer factory helps creating pre-configured stemmer """
    APC_KEY = 'sastrawi_cache_dictionary'

    def create_stemmer(self, isDev=False):
        """ Returns Stemmer instance """

        words = self.get_words(isDev)
        dictionary = ArrayDictionary(words)
        stemmer = Stemmer(dictionary)

        resultCache = ArrayCache()
        cachedStemmer = CachedStemmer(resultCache, stemmer)

        return cachedStemmer

    def get_words(self, isDev=False):
        return self.get_words_from_file()

    def get_words_from_file(self):
        current_dir = os.path.dirname(os.path.realpath(__file__))
        dictionaryFile = os.path.join(current_dir, 'data', 'kata-dasar.txt')
        if not os.path.isfile(dictionaryFile):
            raise RuntimeError('Dictionary file is missing. It seems that your installation is corrupted.')

        dictionaryContent = ''
        with open(dictionaryFile, 'r', encoding='utf-8') as f:
            dictionaryContent = f.read()

        return dictionaryContent.split('\n')