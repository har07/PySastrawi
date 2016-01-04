import re

class DisambiguatorPrefixRule6a(object):
    """Disambiguate Prefix Rule 6a
    Rule 6a : terV -> ter-V
    """
    
    def disambiguate(self, word):
        """Disambiguate Prefix Rule 6a
        Rule 6a : terV -> ter-V
        """
        matches = re.match(r'^ter([aiueo].*)$', word)
        if matches:
            return matches.group(1)
