import re

class DisambiguatorPrefixRule11(object):
    """Disambiguate Prefix Rule 11
    Rule 11 : mem{b|f|v} -> mem-{b|f|v}
    """
    
    def disambiguate(self, word):
        """Disambiguate Prefix Rule 11
        Rule 11 : mem{b|f|v} -> mem-{b|f|v}
        """
        matches = re.match(r'^mem([bfv])(.*)$', word)
        if matches:
            return matches.group(1) + matches.group(2)
