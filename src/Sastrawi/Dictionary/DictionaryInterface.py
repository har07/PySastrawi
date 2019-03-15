# @update_by Mufid Jamaluddin
# @update_date 16/03/2019

from abc import ABCMeta, abstractmethod

class DictionaryInterface:
    """Interface definition of dictionary"""
    __metaclass__ = ABCMeta

    @abstractmethod
    def contains(self, word):
        pass