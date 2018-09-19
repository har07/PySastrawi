class StopWordRemover(object):
    """description of class"""

    def __init__(self, dictionary):
        self.dictionary = dictionary

    def get_dictionary(self):
        return self.dictionary

    def remove(self, text, min_length: int = 1):
        """Remove stop words."""
        words = text.split(' ')
        stopped_words = [word for word in words if not self.dictionary.contains(word) and len(word) >= min_length]

        return ' '.join(stopped_words)
