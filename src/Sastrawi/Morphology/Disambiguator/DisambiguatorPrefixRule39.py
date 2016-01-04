import re

class DisambiguatorPrefixRule39a(object):
    """Disambiguate Prefix Rule 39a (CC infix rules)
    Rule 39a : CemV -> CemV
    """
    
    def disambiguate(self, word):
        """Disambiguate Prefix Rule 39a (CC infix rules)
        Rule 39a : CemV -> CemV
        """
        matches = re.match(r'^([bcdfghjklmnpqrstvwxyz])(em[aiueo])(.*)$', word)
        if matches:
            return matches.group(1) + matches.group(2) + matches.group(3)

class DisambiguatorPrefixRule39b(object):
    """Disambiguate Prefix Rule 39b (CC infix rules)
    Rule 39b : CemV -> CV
    """
    
    def disambiguate(self, word):
        """Disambiguate Prefix Rule 39b (CC infix rules)
        Rule 39b : CemV -> CV
        """
        matches = re.match(r'^([bcdfghjklmnpqrstvwxyz])em([aiueo])(.*)$', word)
        if matches:
            return matches.group(1) + matches.group(2) + matches.group(3)
