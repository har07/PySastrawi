import re

class DisambiguatorPrefixRule25(object):
    """Disambiguate Prefix Rule 25
    Rule 25 : pem{b|f|v} -> pem-{b|f|v}
    """
    
    def disambiguate(self, word):
        """Disambiguate Prefix Rule 25
        Rule 25 : pem{b|f|v} -> pem-{b|f|v}
        """
        matches = re.match(r'^pem([bfv])(.*)$', word)
        if matches:
            return matches.group(1) + matches.group(2)
