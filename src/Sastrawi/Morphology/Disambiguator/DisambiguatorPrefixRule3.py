import re

class DisambiguatorPrefixRule3(object):
    """Disambiguate Prefix Rule 3
    Rule 3 : berCAerV -> ber-CAerV where C != 'r'
    """
    
    def disambiguate(self, word):
        """Disambiguate Prefix Rule 3
        Rule 3 : berCAerV -> ber-CAerV where C != 'r'
        """
        matches = re.match(r'ber([bcdfghjklmnpqrstvwxyz])([a-z])er([aiueo])(.*)', word)
        if matches:
            if matches.group(1) == 'r':
                return
            
            return matches.group(1) + matches.group(2) + 'er' + matches.group(3) + matches.group(4)
