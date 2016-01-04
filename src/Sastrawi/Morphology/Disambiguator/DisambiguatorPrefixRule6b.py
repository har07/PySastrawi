import re

class DisambiguatorPrefixRule6b(object):
    """Disambiguate Prefix Rule 6b
    Rule 6b : terV -> te-rV
    """
    
    def disambiguate(self, word):
        """Disambiguate Prefix Rule 6b
        Rule 6b : terV -> te-rV
        """
        matches = re.match(r'^ter([aiueo].*)$', word)
        if matches:
            return 'r' + matches.group(1)
