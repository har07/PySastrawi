import re

class DisambiguatorPrefixRule34(object):
    """Disambiguate Prefix Rule 34
    Rule 34 : peCP -> pe-CP where C != {r|w|y|l|m|n} and P != 'er'
    """
    
    def disambiguate(self, word):
        """Disambiguate Prefix Rule 34
        Rule 34 : peCP -> pe-CP where C != {r|w|y|l|m|n} and P != 'er'
        """
        matches = re.match(r'^pe([bcdfghjklmnpqrstvwxyz])(.*)$', word)
        if matches:
            if re.match(r'^er(.*)$', matches.group(2)):
                return
            return matches.group(1) + matches.group(2)
