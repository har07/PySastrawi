import re

class DisambiguatorPrefixRule23(object):
    """Disambiguate Prefix Rule 23
    Rule 23 : perCAP -> per-CAP where C != 'r' AND P != 'er'
    """
    
    def disambiguate(self, word):
        """Disambiguate Prefix Rule 23
        Rule 23 : perCAP -> per-CAP where C != 'r' AND P != 'er'
        """
        matches = re.match(r'^per([bcdfghjklmnpqrstvwxyz])([a-z])(.*)$', word)
        if matches:
            if re.match(r'^er(.*)$', matches.group(3)):
                return
            return matches.group(1) + matches.group(2) + matches.group(3)
