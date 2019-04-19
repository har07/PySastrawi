import re


class DisambiguatorPrefixRule24(object):
    """Disambiguate Prefix Rule 24
    Rule 24 : perCAerV -> per-CAerV where C != 'r'
    """

    def disambiguate(self, word):
        """Disambiguate Prefix Rule 24
        Rule 24 : perCAerV -> per-CAerV where C != 'r'
        """
        matches = re.match(r'^per([bcdfghjklmnpqrstvwxyz])([a-z])er([aiueo])(.*)$', word)
        if matches:
            if matches.group(1) == 'r':
                return
            return matches.group(1) + matches.group(2) + 'er' + matches.group(3) + matches.group(4)
