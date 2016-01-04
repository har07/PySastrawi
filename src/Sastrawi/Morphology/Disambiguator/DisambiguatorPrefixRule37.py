import re

class DisambiguatorPrefixRule37a(object):
    """Disambiguate Prefix Rule 37a (CC infix rules)
    Rule 37a : CerV -> CerV
    """
    
    def disambiguate(self, word):
        """Disambiguate Prefix Rule 37a (CC infix rules)
        Rule 37a : CerV -> CerV
        """
        matches = re.match(r'^([bcdfghjklmnpqrstvwxyz])(er[aiueo])(.*)$', word)
        if matches:
            return matches.group(1) + matches.group(2) + matches.group(3)

class DisambiguatorPrefixRule37b(object):
    """Disambiguate Prefix Rule 37b (CC infix rules)
    Rule 37b : CerV -> CV
    """
    
    def disambiguate(self, word):
        """Disambiguate Prefix Rule 37b (CC infix rules)
        Rule 37b : CerV -> CV
        """
        matches = re.match(r'^([bcdfghjklmnpqrstvwxyz])er([aiueo])(.*)$', word)
        if matches:
            return matches.group(1) + matches.group(2) + matches.group(3)
