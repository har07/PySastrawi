import re

class DisambiguatorPrefixRule30a(object):
    """Disambiguate Prefix Rule 30a
    Rule 30a : pengV -> peng-V
    """
    
    def disambiguate(self, word):
        """Disambiguate Prefix Rule 30a
        Rule 30a : pengV -> peng-V
        """
        matches = re.match(r'^peng([aiueo])(.*)$', word)
        if matches:
            return matches.group(1) + matches.group(2)

class DisambiguatorPrefixRule30b(object):
    """Disambiguate Prefix Rule 30b
    Rule 30a : pengV -> peng-kV
    """
    
    def disambiguate(self, word):
        """Disambiguate Prefix Rule 30b
        Rule 30a : pengV -> peng-kV
        """
        matches = re.match(r'^peng([aiueo])(.*)$', word)
        if matches:
            return 'k' + matches.group(1) + matches.group(2)

class DisambiguatorPrefixRule30c(object):
    """Disambiguate Prefix Rule 30c
    Rule 30a : pengV -> pengV- where V = 'e'
    """
    
    def disambiguate(self, word):
        """Disambiguate Prefix Rule 30c
        Rule 30a : pengV -> pengV- where V = 'e'
        """
        matches = re.match(r'^penge(.*)$', word)
        if matches:
            return matches.group(1)
