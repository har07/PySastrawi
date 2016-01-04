import re

class DisambiguatorPrefixRule42(object):
    """Disambiguate Prefix Rule 42
    Rule 42 : kauA -> kau-A
    """
    
    def disambiguate(self, word):
        """Disambiguate Prefix Rule 42
        Rule 42 : kauA -> kau-A
        """
        matches = re.match(r'^kau(.*)$', word)
        if matches:
            return matches.group(1)
