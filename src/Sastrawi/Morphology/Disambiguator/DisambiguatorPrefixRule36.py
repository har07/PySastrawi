import re

class DisambiguatorPrefixRule36(object):
    """Disambiguate Prefix Rule 36
    Rule 36 : peC1erC2 -> pe-C1erC2 where C1 != {r|w|y|l|m|n}
    """
    
    def disambiguate(self, word):
        """Disambiguate Prefix Rule 36
        Rule 36 : peC1erC2 -> pe-C1erC2 where C1 != {r|w|y|l|m|n}
        """
        matches = re.match(r'^pe([bcdfghjkpqstvxz])(er[bcdfghjklmnpqrstvwxyz])(.*)$', word)
        if matches:
            return matches.group(1) + matches.group(2) + matches.group(3)
