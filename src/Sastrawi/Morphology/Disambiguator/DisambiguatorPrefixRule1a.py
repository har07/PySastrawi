import re

class DisambiguatorPrefixRule1a(object):
    """Disambiguate Prefix Rule 1a
    Rule 1a : berV -> ber-V
    """
    
    def disambiguate(self, word):
        """Disambiguate Prefix Rule 1a
        Rule 1a : berV -> ber-V
        """
        matches = re.match(r'^ber([aiueo].*)$', word)
        if matches:
            return matches.group(1)

