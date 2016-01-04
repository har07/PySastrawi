import re

class DisambiguatorPrefixRule17a(object):
    """Disambiguate Prefix Rule 17a
    Rule 17a : mengV -> meng-V
    """
    
    def disambiguate(self, word):
        """Disambiguate Prefix Rule 17a
        Rule 17a : mengV -> meng-V
        """
        matches = re.match(r'^meng([aiueo])(.*)$', word)
        if matches:
            return matches.group(1) + matches.group(2)

class DisambiguatorPrefixRule17b(object):
    """Disambiguate Prefix Rule 17b
    Rule 17b : mengV -> meng-kV
    """
    
    def disambiguate(self, word):
        """Disambiguate Prefix Rule 17b
        Rule 17b : mengV -> meng-kV
        """
        matches = re.match(r'^meng([aiueo])(.*)$', word)
        if matches:
            return 'k' + matches.group(1) + matches.group(2)

class DisambiguatorPrefixRule17c(object):
    """Disambiguate Prefix Rule 17c
    Rule 17c : mengV -> meng-V- where V = 'e'
    """
    
    def disambiguate(self, word):
        """Disambiguate Prefix Rule 17c
        Rule 17c : mengV -> meng-V- where V = 'e'
        """
        matches = re.match(r'^menge(.*)$', word)
        if matches:
            return matches.group(1)

class DisambiguatorPrefixRule17d(object):
    """Disambiguate Prefix Rule 17d
    Rule 17d : mengV -> me-ngV
    """
    
    def disambiguate(self, word):
        """Disambiguate Prefix Rule 17d
        Rule 17d : mengV -> me-ngV
        """
        matches = re.match(r'^meng([aiueo])(.*)$', word)
        if matches:
            return 'ng' + matches.group(1) + matches.group(2)
