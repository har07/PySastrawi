import re

class DisambiguatorPrefixRule9(object):
    """Disambiguate Prefix Rule 9
    Rule 9 : te-C1erC2 -> te-C1erC2 where C1 != 'r'
    """
    
    def disambiguate(self, word):
        """Disambiguate Prefix Rule 9
        Rule 9 : te-C1erC2 -> te-C1erC2 where C1 != 'r'
        """
        matches = re.match(r'^te([bcdfghjklmnpqrstvwxyz])er([bcdfghjklmnpqrstvwxyz])(.*)$', word)
        if matches:
            if matches.group(1) == 'r':
                return
            return matches.group(1) + 'er' + matches.group(2) + matches.group(3)
