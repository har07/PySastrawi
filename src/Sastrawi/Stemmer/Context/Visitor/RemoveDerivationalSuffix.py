import re
from Sastrawi.Stemmer.Context.Removal import Removal

class RemoveDerivationalSuffix(object):
    """Remove Derivational Suffix.
    Asian J. (2007) "Effective Techniques for Indonesian Text Retrieval". page 61

    @link http://researchbank.rmit.edu.au/eserv/rmit:6312/Asian.pdf
    """

    def visit(self, context):
        result = self.remove(context.getCurrentWord())
        if result != context.getCurrentWord():
            removedPart = re.sub(result, '', context.getCurrentWord(), 1)

        removal = Removal(self, context.getCurrentWord(), result, removedPart, 'DS')

        context.addRemoval(removal)
        context.setCurrentWord(result)

    def remove(self, word):
        """Remove derivational suffix
        Original rule : i|kan|an
        Added the adopted foreign suffix rule : is|isme|isasi
        """
        return re.sub(r'(is|isme|isasi|i|kan|an)$', '', word, 1)


