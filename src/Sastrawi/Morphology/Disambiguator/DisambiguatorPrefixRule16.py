import re

class DisambiguatorPrefixRule16(object):
    """Disambiguate Prefix Rule 16
    Original Nazief and Adriani's Rule 16 : meng{g|h|q} -> meng-{g|h|q}
    Modified Jelita Asian's CS Rule 16 : meng{g|h|q|k} -> meng-{g|h|q|k} to stem mengkritik
    """
    
    def disambiguate(self, word):
        """Disambiguate Prefix Rule 16
        Original Nazief and Adriani's Rule 16 : meng{g|h|q} -> meng-{g|h|q}
        Modified Jelita Asian's CS Rule 16 : meng{g|h|q|k} -> meng-{g|h|q|k} to stem mengkritik
        """
        matches = re.match(r'^meng([g|h|q|k])(.*)$', word)
        if matches:
            return matches.group(1) + matches.group(2)
