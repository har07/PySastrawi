import re

class DisambiguatorPrefixRule19(object):
    """Disambiguate Prefix Rule 19
    Original Rule 19 : mempV -> mem-pV where V != 'e'
    Modified Rule 19 by ECS : mempA -> mem-pA where A != 'e' in order to stem memproteksi
    """
    
    def disambiguate(self, word):
        """Disambiguate Prefix Rule 19
        Original Rule 19 : mempV -> mem-pV where V != 'e'
        Modified Rule 19 by ECS : mempA -> mem-pA where A != 'e' in order to stem memproteksi
        """
        matches = re.match(r'^memp([abcdfghijklmopqrstuvwxyz])(.*)$', word)
        if matches:
            return 'p' + matches.group(1) + matches.group(2)
