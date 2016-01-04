import re

class DisambiguatorPrefixRule14(object):
    """Disambiguate Prefix Rule 14
    Rule 14 modified by Andy Librian : men{c|d|j|s|t|z} -> men-{c|d|j|s|t|z}
    in order to stem mentaati
  
    Rule 14 modified by ECS: men{c|d|j|s|z} -> men-{c|d|j|s|z}
    in order to stem mensyaratkan, mensyukuri
  
    Original CS Rule no 14 was : men{c|d|j|z} -> men-{c|d|j|z}
    """
    
    def disambiguate(self, word):
        """Disambiguate Prefix Rule 14
        Rule 14 modified by Andy Librian : men{c|d|j|s|t|z} -> men-{c|d|j|s|t|z}
        in order to stem mentaati
  
        Rule 14 modified by ECS: men{c|d|j|s|z} -> men-{c|d|j|s|z}
        in order to stem mensyaratkan, mensyukuri
  
        Original CS Rule no 14 was : men{c|d|j|z} -> men-{c|d|j|z}
        """
        matches = re.match(r'^men([cdjstz])(.*)$', word)
        if matches:
            return matches.group(1) + matches.group(2)
