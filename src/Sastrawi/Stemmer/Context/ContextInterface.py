from abc import ABCMeta, abstractmethod

class ContextInterface:
    """description of abs class"""
    __metaclass__ = ABCMeta

    @abstractmethod
    def getOriginalWord(self):
        pass

    @abstractmethod
    def setCurrentWord(self, word):
        pass

    @abstractmethod
    def getCurrentWord(self):
        pass

    @abstractmethod
    def getDictionary(self):
        pass

    @abstractmethod
    def stopProcess(self):
        pass

    @abstractmethod
    def processIsStopped(self):
        pass

    @abstractmethod
    def addRemoval(self, removal):
        pass

    @abstractmethod
    def getRemovals(self):
        pass