import re

class DisambiguatorPrefixRule28a(object):
    """Disambiguate Prefix Rule 28a
    Rule 28a : pen{V} -> pe-n{V}
    """
    
    def disambiguate(self, word):
        """Disambiguate Prefix Rule 28a
        Rule 28a : pen{V} -> pe-n{V}
        """
        matches = re.match(r'^pen([aiueo])(.*)$', word)
        if matches:
            return 'n' + matches.group(1) + matches.group(2)

class DisambiguatorPrefixRule28b(object):
    """Disambiguate Prefix Rule 28b
    Rule 28b : pen{V} -> pe-t{V}
    """
    
    def disambiguate(self, word):
        """Disambiguate Prefix Rule 28b
        Rule 28b : pen{V} -> pe-t{V}
        """
        matches = re.match(r'^pen([aiueo])(.*)$', word)
        if matches:
            return 't' + matches.group(1) + matches.group(2)
