class StopWordRemover(object):
    """description of class"""

    def __init__(self, dictionary):
        self.dictionary = dictionary

    def get_dictionary(self):
        return self.dictionary

    def remove(self, text):
        """Remove stop words."""
        words = text.split(' ')
        stopped_words = [word for word in words if not self.dictionary.contains(word)]

        return ' '.join(stopped_words)




