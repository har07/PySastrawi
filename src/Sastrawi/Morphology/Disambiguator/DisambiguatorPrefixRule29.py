import re

class DisambiguatorPrefixRule29(object):
    """Disambiguate Prefix Rule 29
    Original Rule 29 : peng{g|h|q} -> peng-{g|h|q}
    Modified Rule 29 by ECS : pengC -> peng-C
    """
    
    def disambiguate(self, word):
        """Disambiguate Prefix Rule 29
        Original Rule 29 : peng{g|h|q} -> peng-{g|h|q}
        Modified Rule 29 by ECS : pengC -> peng-C
        """
        matches = re.match(r'^peng([bcdfghjklmnpqrstvwxyz])(.*)$', word)
        if matches:
            return matches.group(1) + matches.group(2)
