import re

class DisambiguatorPrefixRule15a(object):
    """Disambiguate Prefix Rule 15a
    Rule 15a : men{V} -> me-n{V}
    """
    
    def disambiguate(self, word):
        """Disambiguate Prefix Rule 15a
        Rule 15a : men{V} -> me-n{V}
        """
        matches = re.match(r'^men([aiueo])(.*)$', word)
        if matches:
            return 'n' + matches.group(1) + matches.group(2)

class DisambiguatorPrefixRule15b(object):
    """Disambiguate Prefix Rule 15b
    Rule 15b : men{V} -> me-t{V}
    """
    
    def disambiguate(self, word):
        """Disambiguate Prefix Rule 15b
        Rule 15b : men{V} -> me-t{V}
        """
        matches = re.match(r'^men([aiueo])(.*)$', word)
        if matches:
            return 't' + matches.group(1) + matches.group(2)
