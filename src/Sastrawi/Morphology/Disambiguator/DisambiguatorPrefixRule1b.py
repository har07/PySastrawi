import re

class DisambiguatorPrefixRule1b(object):
    """Disambiguate Prefix Rule 1b
    Rule 1b : berV -> be-rV
    """
    
    def disambiguate(self, word):
        """Disambiguate Prefix Rule 1b
        Rule 1b : berV -> be-rV
        """
        matches = re.match(r'^ber([aiueo].*)$', word)
        if matches:
            return 'r' + matches.group(1)

