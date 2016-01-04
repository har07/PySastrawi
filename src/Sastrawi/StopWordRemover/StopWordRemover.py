class StopWordRemover(object):
    """description of class"""

    def __init__(self, dictionary):
        self.dictionary = dictionary

    def getDictionary(self):
        return self.dictionary

    def remove(self, text):
        """Remove stop words."""
        words = text.split(' ')
        for word in words:
            if word in self.dictionary:
                self.dictionary.remove(word)

        return ' '.join(words)




