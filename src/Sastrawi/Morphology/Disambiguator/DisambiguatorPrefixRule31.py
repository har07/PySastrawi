import re

class DisambiguatorPrefixRule31a(object):
    """Disambiguate Prefix Rule 31a
    Rule 31a : penyV -> pe-nyV
    """
    
    def disambiguate(self, word):
        """Disambiguate Prefix Rule 31a
        Rule 31a : penyV -> pe-nyV
        """
        matches = re.match(r'^peny([aiueo])(.*)$', word)
        if matches:
            return 'ny' + matches.group(1) + matches.group(2)

class DisambiguatorPrefixRule31b(object):
    """Disambiguate Prefix Rule 31b
    Original Rule 31 : penyV -> peny-sV
    Modified by CC, shifted to 31b
    """
    
    def disambiguate(self, word):
        """Disambiguate Prefix Rule 31b
        Original Rule 31 : penyV -> peny-sV
        Modified by CC, shifted to 31b
        """
        matches = re.match(r'^peny([aiueo])(.*)$', word)
        if matches:
            return 's' + matches.group(1) + matches.group(2)
