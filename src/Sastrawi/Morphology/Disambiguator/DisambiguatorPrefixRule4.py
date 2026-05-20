class DisambiguatorPrefixRule4:
    """Disambiguate Prefix Rule 4
    Rule 4 : belajar -> bel-ajar
    """
    
    def disambiguate(self, word):
        """Disambiguate Prefix Rule 4
        Rule 4 : belajar -> bel-ajar
        """
        if word == 'belajar':
            return 'ajar'
