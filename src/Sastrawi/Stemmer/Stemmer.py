import re
from Sastrawi.Stemmer.Context.Visitor.VisitorProvider import VisitorProvider
from Sastrawi.Stemmer.Filter import TextNormalizer
from Sastrawi.Stemmer.Context.Context import Context

class Stemmer(object):
    """Indonesian Stemmer.
    Nazief & Adriani, CS Stemmer, ECS Stemmer, Improved ECS.

    @link https://github.com/sastrawi/sastrawi/wiki/Resources
    """
    def __init__(self, dictionary):
        self.dictionary = dictionary
        self.visitor_provider = VisitorProvider()

    def get_dictionary(self):
        return self.dictionary

    def stem(self, text):
        """Stem a text string to its common stem form."""
        normalizedText = TextNormalizer.normalize_text(text)

        words = normalizedText.split(' ')
        stems = []

        for word in words:
            stems.append(self.stem_word(word))

        return ' '.join(stems)

    def stem_word(self, word):
        """Stem a word to its common stem form."""
        if self.is_plural(word):
            return self.stem_plural_word(word)
        else:
            return self.stem_singular_word(word)

    def is_plural(self, word):
        #-ku|-mu|-nya
        #nikmat-Ku, etc
        matches = re.match(r'^(.*)-(ku|mu|nya|lah|kah|tah|pun)$', word)
        if matches:
            return matches.group(1).find('-') != -1

        return word.find('-') != -1

    def stem_plural_word(self, plural):
        """Stem a plural word to its common stem form.
        Asian J. (2007) "Effective Techniques for Indonesian Text Retrieval" page 76-77.

        @link   http://researchbank.rmit.edu.au/eserv/rmit:6312/Asian.pdf
        """
        matches = re.match(r'^(.*)-(.*)$', plural)
        #translated from PHP conditional check:
        #if (!isset($words[1]) || !isset($words[2]))
        if not matches:
            return plural
        words = [matches.group(1), matches.group(2)]

        #malaikat-malaikat-nya -> malaikat malaikat-nya
        suffix = words[1]
        suffixes = ['ku', 'mu', 'nya', 'lah', 'kah', 'tah', 'pun']
        matches = re.match(r'^(.*)-(.*)$', words[0])
        if suffix in suffixes and matches:
            words[0] = matches.group(1)
            words[1] = matches.group(2) + '-' + suffix

        #berbalas-balasan -> balas
        rootWord1 = self.stem_singular_word(words[0])
        rootWord2 = self.stem_singular_word(words[1])

        #meniru-nirukan -> tiru
        if not self.dictionary.contains(words[1]) and rootWord2 == words[1]:
            rootWord2 = self.stem_singular_word('me' + words[1])

        if rootWord1 == rootWord2:
            return rootWord1
        else:
            return plural

    def stem_singular_word(self, word):
        """Stem a singular word to its common stem form."""
        context = Context(word, self.dictionary, self.visitor_provider)
        context.execute()

        return context.result

