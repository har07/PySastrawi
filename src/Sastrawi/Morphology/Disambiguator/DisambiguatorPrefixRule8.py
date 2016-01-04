import re

class DisambiguatorPrefixRule8(object):
    """Disambiguate Prefix Rule 8
    Rule 8 : terCP -> ter-CP where C != 'r' and P != 'er'
    """
    
    def disambiguate(self, word):
        """Disambiguate Prefix Rule 8
        Rule 8 : terCP -> ter-CP where C != 'r' and P != 'er'
        """
        matches = re.match(r'^ter([bcdfghjklmnpqrstvwxyz])(.*)$', word)
        if matches:
            if matches.group(1) == 'r' or re.match(r'^er(.*)$', matches.group(2)):
                return
            return matches.group(1) + matches.group(2)
