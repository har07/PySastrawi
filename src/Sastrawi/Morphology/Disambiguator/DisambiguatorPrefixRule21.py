import re

class DisambiguatorPrefixRule21a(object):
    """Disambiguate Prefix Rule 21a
    Rule 21a : perV -> per-V
    """
    
    def disambiguate(self, word):
        """Disambiguate Prefix Rule 21a
        Rule 21a : perV -> per-V
        """
        matches = re.match(r'^per([aiueo])(.*)$', word)
        if matches:
            return matches.group(1) + matches.group(2)

class DisambiguatorPrefixRule21b(object):
    """Disambiguate Prefix Rule 21b
    Rule 21b : perV -> pe-rV
    """
    
    def disambiguate(self, word):
        """Disambiguate Prefix Rule 21b
        Rule 21b : perV -> pe-rV
        """
        matches = re.match(r'^pe(r[aiueo])(.*)$', word)
        if matches:
            return matches.group(1) + matches.group(2)
