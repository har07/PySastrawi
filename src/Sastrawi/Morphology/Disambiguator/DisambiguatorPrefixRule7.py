import re

class DisambiguatorPrefixRule7(object):
    """Disambiguate Prefix Rule 7
    Rule 7 : terCerv -> ter-CerV where C != 'r'
    """
    
    def disambiguate(self, word):
        """Disambiguate Prefix Rule 7
        Rule 7 : terCerv -> ter-CerV where C != 'r'
        """
        matches = re.match(r'^ter([bcdfghjklmnpqrstvwxyz])er([aiueo].*)$', word)
        if matches:
            if matches.group(1) == 'r':
                return
            return matches.group(1) + 'er' + matches.group(2)
