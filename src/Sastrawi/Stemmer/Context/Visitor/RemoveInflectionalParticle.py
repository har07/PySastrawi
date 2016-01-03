import re
from Sastrawi.Stemmer.Context.Removal import Removal

class RemoveInflectionalParticle(object):
    """Remove Inflectional particle.
    Asian J. (2007) "Effective Techniques for Indonesian Text Retrieval". page 60

    @link http://researchbank.rmit.edu.au/eserv/rmit:6312/Asian.pdf
    """

    def visit(self, context):
        result = self.remove(context.getCurrentWord())
        if result != context.getCurrentWord():
            removedPart = re.sub(result, '', context.getCurrentWord(), 1)

        removal = Removal(self, context.getCurrentWord(), result, removedPart, 'P')

        context.addRemoval(removal)
        context.setCurrentWord(result)

    def remove(self, word):
        """Remove inflectional particle : lah|kah|tah|pun"""
        return re.sub(r'-*(lah|kah|tah|pun)$', '', word, 1)



