import re

class DisambiguatorPrefixRule13b(object):
    """Disambiguate Prefix Rule 13b
    Rule 13b : mem{rV|V} -> me-p{rV|V}
    """
    
    def disambiguate(self, word):
        """Disambiguate Prefix Rule 13b
        Rule 13b : mem{rV|V} -> me-p{rV|V}
        """
        matches = re.match(r'^mem([aiueo])(.*)$', word)
        if matches:
            return 'p' + matches.group(1) + matches.group(2)
