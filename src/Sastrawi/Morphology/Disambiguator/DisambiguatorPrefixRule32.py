import re

class DisambiguatorPrefixRule32(object):
    """Disambiguate Prefix Rule 32
    Rule 32 : pelV -> pe-lV except pelajar -> ajar
    """
    
    def disambiguate(self, word):
        """Disambiguate Prefix Rule 32
        Rule 32 : pelV -> pe-lV except pelajar -> ajar
        """
        if word == 'pelajar':
            return 'ajar'
        matches = re.match(r'^pe(l[aiueo])(.*)$', word)
        if matches:
            return matches.group(1) + matches.group(2)
