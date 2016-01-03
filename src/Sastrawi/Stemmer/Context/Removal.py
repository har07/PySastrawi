from Sastrawi.Stemmer.Context.RemovalInterface import RemovalInterface

class Removal(RemovalInterface):
    """description of class"""

    def __init__(self, visitor, subject, result, removedPart, affixType):
        self.visitor = visitor
        self.subject = subject
        self.result = result
        self.removedPart = removedPart
        self.affixType = affixType

    def getVisitor(self):
        return self.visitor

    def getSubject(self):
        return self.subject

    def getResult(self):
        return self.result

    def getRemovedPart(self):
        return self.removedPart

    def getAffixType(self):
        return self.affixType



