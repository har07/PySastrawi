class StopWordRemover(object):
    """description of class"""

    def __init__(self, dictionary):
        self.dictionary = dictionary

    def get_dictionary(self):
        return self.dictionary

    def remove(self, text):
        """Remove stop words."""
        words = text.split(' ')
        for word in words:
            if self.dictionary.contains(word):
                words.remove(word)

        return ' '.join(words)




