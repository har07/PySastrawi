from Sastrawi.Stemmer.Context.RemovalInterface import RemovalInterface

class Removal(RemovalInterface):
    """description of class"""

    def __init__(self, visitor, subject, result, removedPart, affixType):
        self.visitor = visitor
        self.subject = subject
        self.result = result
        self.removedPart = removedPart
        self.affixType = affixType

    def get_visitor(self):
        return self.visitor

    def get_subject(self):
        return self.subject

    def get_result(self):
        return self.result

    def get_removed_part(self):
        return self.removedPart

    def get_affix_type(self):
        return self.affixType



