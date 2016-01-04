import re

class DisambiguatorPrefixRule13a(object):
    """Disambiguate Prefix Rule 13a
    Rule 13a : mem{rV|V} -> me-m{rV|V}
    """
    
    def disambiguate(self, word):
        """Disambiguate Prefix Rule 13a
        Rule 13a : mem{rV|V} -> me-m{rV|V}
        """
        matches = re.match(r'^mem([aiueo])(.*)$', word)
        if matches:
            return 'm' + matches.group(1) + matches.group(2)
