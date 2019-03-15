#from Sastrawi.Stemmer.StemmerInterface import StemmerInterface
from Sastrawi.Stemmer.Filter import TextNormalizer

class CachedStemmer(object):
    """description of class"""
    def __init__(self, cache, delegatedStemmer):
        self.cache = cache
        self.delegatedStemmer = delegatedStemmer

    def stem(self, text):
        normalizedText = TextNormalizer.normalize_text(text)

        words = normalizedText.split(' ')
        stems = []

        for word in words:
            if self.cache.has(word):
                stems.append(self.cache.get(word))
            else:
                stem = self.delegatedStemmer.stem_word(word)
                self.cache.set(word, stem)
                stems.append(stem)

        return ' '.join(stems)

    def stem_word(self, word):
        if self.cache.has(word):
            return self.cache.get(word)
        else:
            stem = self.delegatedStemmer.stem_word(word)
            self.cache.set(word, stem)
            return stem

    def get_cache(self):
        return self.cache
