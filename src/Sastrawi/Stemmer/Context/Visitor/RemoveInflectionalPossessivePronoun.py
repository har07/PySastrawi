import re
from Sastrawi.Stemmer.Context.Removal import Removal

class RemoveInflectionalPossessivePronoun(object):
    """Remove Inflectional Possessive Pronoun
    Asian J. (2007) "Effective Techniques for Indonesian Text Retrieval". page 60
    
    @link http://researchbank.rmit.edu.au/eserv/rmit:6312/Asian.pdf
    """

    def visit(self, context):
        result = self.remove(context.getCurrentWord())
        if result != context.getCurrentWord():
            removedPart = re.sub(result, '', context.getCurrentWord(), 1)

            removal = Removal(self, context.getCurrentWord(), result, removedPart, 'PP')

            context.addRemoval(removal)
            context.setCurrentWord(result)

    def remove(self, word):
        """Remove inflectional possessive pronoun : ku|mu|nya|-ku|-mu|-nya"""
        return re.sub(r'-*(ku|mu|nya)', '', word, 1)

