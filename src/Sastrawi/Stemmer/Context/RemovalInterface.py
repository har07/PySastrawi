from abc import ABCMeta, abstractmethod

class RemovalInterface:
    """description of class"""
    __metaclass__ = ABCMeta

    @abstractmethod
    def get_visitor(self):
        pass

    @abstractmethod
    def get_subject(self):
        pass

    @abstractmethod
    def get_result(self):
        pass

    @abstractmethod
    def get_removed_part(self):
        pass

    @abstractmethod
    def get_affix_type(self):
        pass




