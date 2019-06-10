import re
import os
from Sastrawi.stemming.context import Context
from Sastrawi.stemming.rules import VisitorProvider

class Stemmer():
    """
    Indonesian Stemmer.
    Nazief & Adriani, CS Stemmer, ECS Stemmer, Improved ECS.

    @link https://github.com/sastrawi/sastrawi/wiki/Resources
    """

    def __init__(self, stemwords=None, stopwords=None):

        current_dir = os.path.dirname(os.path.realpath(__file__))
        err_msg = '{} is missing. It seems that your installation is corrupted'

        if stemwords is None:
            try:
                filepath = '/data/stemwords.txt'
                with open(current_dir + filepath, 'r') as file:
                    words = file.read().split('\n')
                    self.stemwords = set(words)
            except FileNotFoundError:
                raise RuntimeError(err_msg.format(filepath)) from None
        else:
            self.stemwords = stemwords

        if stopwords is None:
            try:
                filepath = '/data/stopwords.txt'
                with open(current_dir + filepath, 'r') as file:
                    words = file.read().split('\n')
                    self.stopwords = set(words)
            except FileNotFoundError:
                raise RuntimeError(err_msg.format(filepath)) from None
        else:
            self.stopwords = stopwords

        self.cache = dict()
        self.visitor_provider = VisitorProvider()

    def stem(self, text):
        """
        Stem a text string to its common stem form.
        """

        # normalize_text
        result = text.lower() # lower the text even unicode given
        result = re.sub(r'[^a-z0-9 -]', ' ', result, flags=re.IGNORECASE|re.MULTILINE)
        result = re.sub(r'( +)', ' ', result, flags=re.IGNORECASE|re.MULTILINE)
        words = result.strip().split(' ')

        stems = list()

        for word in words:
            if word not in self.cache:
                self.cache[word] = self._stem_word(word)
            stems.append(self.cache[word])

        return ' '.join(stems)

    def remove(self, text):
        """
        Remove stop words.
        """

        words = text.lower().split(' ')
        stopped_words = [w for w in words if w not in self.stopwords]

        return ' '.join(stopped_words)

    def _stem_word(self, word):
        """
        Stem a word to its stem form.
        """

        if self._is_plural(word):
            return self._stem_plural_word(word)
        return self._stem_singular_word(word)

    def _is_plural(self, word):
        """
        Check if a word is in plural form.
        """

        # -ku|-mu|-nya
        # nikmat-Ku, etc
        matches = re.match(r'^(.*)-(ku|mu|nya|lah|kah|tah|pun)$', word)
        if matches:
            return matches.group(1).find('-') != -1
        return word.find('-') != -1

    def _stem_plural_word(self, plural):
        """
        Stem a plural word to its common stem form.
        Asian J. (2007) "Effective Techniques for Indonesian Text Retrieval" page 76-77.

        @link   http://researchbank.rmit.edu.au/eserv/rmit:6312/Asian.pdf
        """

        matches = re.match(r'^(.*)-(.*)$', plural)
        # translated from PHP conditional check:
        # if (!isset($words[1]) || !isset($words[2]))
        if not matches:
            return plural
        words = [matches.group(1), matches.group(2)]

        # malaikat-malaikat-nya -> malaikat malaikat-nya
        suffix = words[1]
        suffixes = ['ku', 'mu', 'nya', 'lah', 'kah', 'tah', 'pun']
        matches = re.match(r'^(.*)-(.*)$', words[0])
        if suffix in suffixes and matches:
            words[0] = matches.group(1)
            words[1] = matches.group(2) + '-' + suffix

        # berbalas-balasan -> balas
        root_word1 = self._stem_singular_word(words[0])
        root_word2 = self._stem_singular_word(words[1])

        # meniru-nirukan -> tiru
        if not words[1] in self.stemwords and root_word2 == words[1]:
            root_word2 = self._stem_singular_word('me' + words[1])

        if root_word1 == root_word2:
            return root_word1
        return plural

    def _stem_singular_word(self, word):
        """
        Stem a singular word to its common stem form.
        """

        return Context(word, self.stemwords, self.visitor_provider).result
