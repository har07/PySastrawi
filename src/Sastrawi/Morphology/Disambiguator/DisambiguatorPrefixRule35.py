import re

class DisambiguatorPrefixRule35(object):
    """Disambiguate Prefix Rule 35
    Rule 35 : terC1erC2 -> ter-C1erC2 where C1 != {r}
    """
    
    def disambiguate(self, word):
        """Disambiguate Prefix Rule 35
        Rule 35 : terC1erC2 -> ter-C1erC2 where C1 != {r}
        """
        matches = re.match(r'^ter([bcdfghjkpqstvxz])(er[bcdfghjklmnpqrstvwxyz])(.*)$', word)
        if matches:
            return matches.group(1) + matches.group(2) + matches.group(3)
