import re

class DisambiguatorPrefixRule27(object):
    """Disambiguate Prefix Rule 27
    Rule 27 modified by Prasasto Adi : pen{c|d|j|s|t|z} -> pen-{c|d|j|s|t|z}
    in order to stem penstabilan, pentranskripsi

    Original CS Rule 27 was : pen{c|d|j|z} -> pen-{c|d|j|z}
    """
    
    def disambiguate(self, word):
        """Disambiguate Prefix Rule 27
        Rule 27 modified by Prasasto Adi : pen{c|d|j|s|t|z} -> pen-{c|d|j|s|t|z}
        in order to stem penstabilan, pentranskripsi

        Original CS Rule 27 was : pen{c|d|j|z} -> pen-{c|d|j|z}
        """
        matches = re.match(r'^pen([cdjstz])(.*)$', word)
        if matches:
            return matches.group(1) + matches.group(2)
