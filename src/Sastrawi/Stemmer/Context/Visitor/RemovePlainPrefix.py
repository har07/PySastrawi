import re
from Sastrawi.Stemmer.Context.Removal import Removal

class RemovePlainPrefix(object):
    """Remove Plain Prefix.
    Asian J. (2007) "Effective Techniques for Indonesian Text Retrieval". page 61

    @link http://researchbank.rmit.edu.au/eserv/rmit:6312/Asian.pdf
    """

    def visit(self, context):
        result = self.remove(context.current_word)
        if result != context.current_word:
            removedPart = re.sub(result, '', context.current_word, 1)

            removal = Removal(self, context.current_word, result, removedPart, 'DP')

            context.add_removal(removal)
            context.current_word = result

    def remove(self, word):
        """Remove plain prefix : di|ke|se"""
        return re.sub(r'^(di|ke|se)', '', word, 1)








