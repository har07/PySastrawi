from Sastrawi.Stemmer.Context.Visitor.AbstractDisambiguatePrefixRule import AbstractDisambiguatePrefixRule

class PrefixDisambiguator(AbstractDisambiguatePrefixRule):
    """description of class"""

    def __init__(self, disambiguators):
        super(PrefixDisambiguator, self).__init__()

        self.add_disambiguators(disambiguators)



