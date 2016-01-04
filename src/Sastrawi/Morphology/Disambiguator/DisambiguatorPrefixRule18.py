import re

class DisambiguatorPrefixRule18a(object):
    """Disambiguate Prefix Rule 18a
    Rule 18a : menyV -> me-nyV to stem menyala -> nyala
    """
    
    def disambiguate(self, word):
        """Disambiguate Prefix Rule 18a
        Rule 18a : menyV -> me-nyV to stem menyala -> nyala
        """
        matches = re.match(r'^meny([aiueo])(.*)$', word)
        if matches:
            return 'ny' + matches.group(1) + matches.group(2)

class DisambiguatorPrefixRule18b(object):
    """Disambiguate Prefix Rule 18a
    Original Rule 18 : menyV -> meny-sV
    Modified by CC (shifted into 18b, see also 18a)
    """
    
    def disambiguate(self, word):
        """Disambiguate Prefix Rule 18a
        Original Rule 18 : menyV -> meny-sV
        Modified by CC (shifted into 18b, see also 18a)
        """
        matches = re.match(r'^meny([aiueo])(.*)$', word)
        if matches:
            return 's' + matches.group(1) + matches.group(2)
