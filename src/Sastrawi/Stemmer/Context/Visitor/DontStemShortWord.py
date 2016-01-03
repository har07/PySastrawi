class DontStemShortWord(object):
    """description of class"""

    def visit(self, context):
        if self.isShortWord(context.getCurrentWord()):
            context.stopProcess()

    def isShortWord(self, word):
        return len(word) <= 3




