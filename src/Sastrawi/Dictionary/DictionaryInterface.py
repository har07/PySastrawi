from abc import ABCMeta, abstractmethod

class DictionaryInterface:
    """Interface definition of dictionary"""
    __metaclass__ = ABCMeta

    @abstractmethod
    def contains(self, word):
        pass