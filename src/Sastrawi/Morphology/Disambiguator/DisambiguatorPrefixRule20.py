import re

class DisambiguatorPrefixRule20(object):
    """Disambiguate Prefix Rule 20
    Rule 20 : pe{w|y}V -> pe-{w|y}V
    """
    
    def disambiguate(self, word):
        """Disambiguate Prefix Rule 20
        Rule 20 : pe{w|y}V -> pe-{w|y}V
        """
        matches = re.match(r'^pe([wy])([aiueo])(.*)$', word)
        if matches:
            return matches.group(1) + matches.group(2) + matches.group(3)
