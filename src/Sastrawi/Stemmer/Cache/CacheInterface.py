# @update_by Mufid Jamaluddin
# @update_date 16/03/2019

from abc import ABCMeta, abstractmethod

class CacheInterface:
    """description of abs class"""
    __metaclass__ = ABCMeta

    @abstractmethod
    def has(self, key):
        pass

    @abstractmethod
    def set(self, key, value):
        pass

    @abstractmethod
    def get(self, key):
        pass