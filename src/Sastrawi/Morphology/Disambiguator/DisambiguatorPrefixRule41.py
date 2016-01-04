import re

class DisambiguatorPrefixRule41(object):
    """Disambiguate Prefix Rule 41
    Rule 41 : kuA -> ku-A
    """
    
    def disambiguate(self, word):
        """Disambiguate Prefix Rule 41
        Rule 41 : kuA -> ku-A
        """
        matches = re.match(r'^ku(.*)$', word)
        if matches:
            return matches.group(1)
