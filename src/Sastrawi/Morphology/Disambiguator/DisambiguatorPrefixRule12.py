import re

class DisambiguatorPrefixRule12(object):
    """Disambiguate Prefix Rule 12
    Nazief and Adriani Rule 12 : beC1erC2 -> be-C1erC2 where C1 != 'r'
    Modified by Jelita Asian's CS Rule 12 : mempe -> mem-pe to stem mempengaruhi
    """
    
    def disambiguate(self, word):
        """Disambiguate Prefix Rule 12
        Nazief and Adriani Rule 12 : beC1erC2 -> be-C1erC2 where C1 != 'r'
        Modified by Jelita Asian's CS Rule 12 : mempe -> mem-pe to stem mempengaruhi
        """
        matches = re.match(r'^mempe(.*)$', word)
        if matches:
            return 'pe' + matches.group(1)
