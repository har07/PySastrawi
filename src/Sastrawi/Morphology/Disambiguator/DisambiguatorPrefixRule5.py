import re

class DisambiguatorPrefixRule5(object):
    """Disambiguate Prefix Rule 5
    Rule 5 : beC1erC2 -> be-C1erC2 where C1 != 'r'
    """
    
    def disambiguate(self, word):
        """Disambiguate Prefix Rule 5
        Rule 5 : beC1erC2 -> be-C1erC2 where C1 != 'r'
        """
        matches = re.match(r'be([bcdfghjklmnpqstvwxyz])(er[bcdfghjklmnpqrstvwxyz])(.*)$', word)
        if matches:
            return matches.group(1) + matches.group(2) + matches.group(3)
