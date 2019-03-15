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

    # Remove Stopword in Tokens
    # @author Mufid Jamaluddin <mufidjamaluddin@outlook.com>
    def remove_tokens(self, tokens:list):
        clean_tokens = [token for token in tokens if not self.dictionary.contains(token)]
        return clean_tokens