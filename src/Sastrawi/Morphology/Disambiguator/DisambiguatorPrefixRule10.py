import re

class DisambiguatorPrefixRule10(object):
    """Disambiguate Prefix Rule 10
    Rule 10 : me{l|r|w|y}V -> me-{l|r|w|y}V
    """
    
    def disambiguate(self, word):
        """Disambiguate Prefix Rule 10
        Rule 10 : me{l|r|w|y}V -> me-{l|r|w|y}V
        """
        matches = re.match(r'^me([lrwy])([aiueo])(.*)$', word)
        if matches:
            return matches.group(1) + matches.group(2) + matches.group(3)
