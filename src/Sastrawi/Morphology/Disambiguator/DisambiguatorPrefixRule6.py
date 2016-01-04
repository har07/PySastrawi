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
