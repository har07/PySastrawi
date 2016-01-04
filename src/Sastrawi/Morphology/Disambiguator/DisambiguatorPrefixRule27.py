import re

class DisambiguatorPrefixRule27(object):
    """Disambiguate Prefix Rule 27
    Rule 27 : pen{c|d|j|z} -> pen-{c|d|j|z}
    """
    
    def disambiguate(self, word):
        """Disambiguate Prefix Rule 27
        Rule 27 : pen{c|d|j|z} -> pen-{c|d|j|z}
        """
        matches = re.match(r'^pen([cdjz])(.*)$', word)
        if matches:
            return matches.group(1) + matches.group(2)
