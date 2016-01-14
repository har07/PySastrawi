class ArrayDictionary(object):
    """description of class"""

    def __init__(self, words=None):
        self.words = []
        if words:
            self.add_words(words)

    def contains(self, word):
        return word in self.words

    def count(self):
        return len(self.words)

    def add_words(self, words):
        """Add multiple words to the dictionary"""
        for word in words:
            self.add(word)

    def add(self, word):
        """Add a word to the dictionary"""
        if not word or word.strip() == '':
            return
        self.words.append(word)





