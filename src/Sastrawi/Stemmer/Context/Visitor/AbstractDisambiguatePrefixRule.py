import re
from Sastrawi.Stemmer.Context.Removal import Removal

class AbstractDisambiguatePrefixRule(object):
    """description of class"""

    def __init__(self):
        self.disambiguators = []

    def visit(self, context):
        result = None

        for disambiguator in self.disambiguators:
            result = disambiguator.disambiguate(context.getCurrentWord())
            if context.getDictionary().contains(result):
                break

        if not result:
            return

        removedPart = re.sub(result, '', context.getCurrentWord(), 1)

        removal = Removal(self, context.getCurrentWord(), result, removedPart, 'DP')

        context.addRemoval(removal)
        context.setCurrentWord(result)

    def addDisambiguators(self, disambiguators):
        for disambiguator in disambiguators:
            self.addDisambiguator(disambiguator)

    def addDisambiguator(self, disambiguator):
        self.disambiguators.append(disambiguator)



