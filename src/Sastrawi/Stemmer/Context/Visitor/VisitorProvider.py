from Sastrawi.Stemmer.Context.Visitor.DontStemShortWord import DontStemShortWord
from Sastrawi.Stemmer.Context.Visitor.RemoveInflectionalParticle import RemoveInflectionalParticle
from Sastrawi.Stemmer.Context.Visitor.RemoveDerivationalSuffix import RemoveDerivationalSuffix
from Sastrawi.Stemmer.Context.Visitor.RemoveInflectionalPossessivePronoun import RemoveInflectionalPossessivePronoun
from Sastrawi.Stemmer.Context.Visitor.Disambiguators import PrefixDisambiguator
from Sastrawi.Stemmer.Context.Visitor.Disambiguators import DisambiguatorsPrefixRule as DPR
from Sastrawi.Stemmer.Context.Visitor.RemovePlainPrefix import RemovePlainPrefix


class VisitorProvider(object):
    """description of class"""

    def __init__(self):
        self.visitors = []
        self.suffix_visitors = []
        self.prefix_visitors = []

        self.visitors.append(DontStemShortWord())

        #{lah|kah|tah|pun}
        self.suffix_visitors.append(RemoveInflectionalParticle())
        #{ku|mu|nya}
        self.suffix_visitors.append(RemoveInflectionalPossessivePronoun())
        #{i|kan|an}
        self.suffix_visitors.append(RemoveDerivationalSuffix())

        #{di|ke|se}
        self.prefix_visitors.append(RemovePlainPrefix())

        # Add all (42) rule in DisambiguatorsPrefixRule to prefix_visitors
        name_list = dir(DPR)
        for n in range(1,43):
            rule_list = [getattr(DPR(), rule) for rule in name_list if str(n) in rule]
            self.prefix_visitors.append(PrefixDisambiguator(rule_list))
