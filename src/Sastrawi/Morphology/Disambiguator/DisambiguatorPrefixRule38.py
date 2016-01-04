import re

class DisambiguatorPrefixRule38a(object):
    """Disambiguate Prefix Rule 38a (CC infix rules)
    Rule 38a : CelV -> CelV
    """
    
    def disambiguate(self, word):
        """Disambiguate Prefix Rule 38a (CC infix rules)
        Rule 38a : CelV -> CelV
        """
        matches = re.match(r'^([bcdfghjklmnpqrstvwxyz])(el[aiueo])(.*)$', word)
        if matches:
            return matches.group(1) + matches.group(2) + matches.group(3)

class DisambiguatorPrefixRule38b(object):
    """Disambiguate Prefix Rule 38b (CC infix rules)
    Rule 38b : CelV -> CV
    """
    
    def disambiguate(self, word):
        """Disambiguate Prefix Rule 38b (CC infix rules)
        Rule 38b : CelV -> CV
        """
        matches = re.match(r'^([bcdfghjklmnpqrstvwxyz])el([aiueo])(.*)$', word)
        if matches:
            return matches.group(1) + matches.group(2) + matches.group(3)
