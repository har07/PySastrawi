from Sastrawi.Stemmer.Cache.CacheInterface import CacheInterface

class ArrayCache(CacheInterface):
    """description of class"""

    def __init__(self):
        self.data = {}

    def set(self, key, value):
        self.data[key] = value

    def get(self, key):
        if key in self.data:
            return self.data[key]

    def has(self, key):
        return key in self.data


