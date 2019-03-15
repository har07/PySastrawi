class ArrayDictionary(object):
    """description of class"""

    def __init__(self, words=None):

		if words is dict:
			self.words = words

        if words is list:
			self.words = {}
            self.add_words(words)

    def contains(self, word):
        return word in self.words

    def count(self):
        return len(self.words)

    def add_words(self, words):
        """Add multiple words to the dictionary"""
        self.words = dict(zip(words,words))

    def add(self, word):
        """Add a word to the dictionary"""
        if not word or word.strip() == '':
            return
        self.words[word]=word





