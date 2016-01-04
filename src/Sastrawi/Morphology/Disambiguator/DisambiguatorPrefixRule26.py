import re

class DisambiguatorPrefixRule26a(object):
    """Disambiguate Prefix Rule 26a
    Rule 26a : pem{rV|V} -> pe-m{rV|V}
    """
    
    def disambiguate(self, word):
        """Disambiguate Prefix Rule 26a
        Rule 26a : pem{rV|V} -> pe-m{rV|V}
        """
        matches = re.match(r'^pem([aiueo])(.*)$', word)
        if matches:
            return 'm' + matches.group(1) + matches.group(2)

class DisambiguatorPrefixRule26b(object):
    """Disambiguate Prefix Rule 26b
    Rule 26b : pem{rV|V} -> pe-p{rV|V}
    """
    
    def disambiguate(self, word):
        """Disambiguate Prefix Rule 26b
        Rule 26b : pem{rV|V} -> pe-p{rV|V}
        """
        matches = re.match(r'^pem([aiueo])(.*)$', word)
        if matches:
            return 'p' + matches.group(1) + matches.group(2)
