from Sastrawi.Stemmer.Context.Visitor.DontStemShortWord import DontStemShortWord
from Sastrawi.Stemmer.Context.Visitor.RemoveInflectionalParticle import RemoveInflectionalParticle
from Sastrawi.Stemmer.Context.Visitor.RemoveDerivationalSuffix import RemoveDerivationalSuffix
from Sastrawi.Stemmer.Context.Visitor.RemoveInflectionalPossessivePronoun import RemoveInflectionalPossessivePronoun
from Sastrawi.Stemmer.Context.Visitor.PrefixDisambiguator import PrefixDisambiguator
from Sastrawi.Stemmer.Context.Visitor.RemovePlainPrefix import RemovePlainPrefix

from Sastrawi.Morphology.Disambiguator.DisambiguatorPrefixRule1a import DisambiguatorPrefixRule1a
from Sastrawi.Morphology.Disambiguator.DisambiguatorPrefixRule1b import DisambiguatorPrefixRule1b
from Sastrawi.Morphology.Disambiguator.DisambiguatorPrefixRule2 import DisambiguatorPrefixRule2
from Sastrawi.Morphology.Disambiguator.DisambiguatorPrefixRule3 import DisambiguatorPrefixRule3
from Sastrawi.Morphology.Disambiguator.DisambiguatorPrefixRule4 import DisambiguatorPrefixRule4
from Sastrawi.Morphology.Disambiguator.DisambiguatorPrefixRule5 import DisambiguatorPrefixRule5
from Sastrawi.Morphology.Disambiguator.DisambiguatorPrefixRule6a import DisambiguatorPrefixRule6a
from Sastrawi.Morphology.Disambiguator.DisambiguatorPrefixRule6b import DisambiguatorPrefixRule6b
from Sastrawi.Morphology.Disambiguator.DisambiguatorPrefixRule7 import DisambiguatorPrefixRule7
from Sastrawi.Morphology.Disambiguator.DisambiguatorPrefixRule8 import DisambiguatorPrefixRule8
from Sastrawi.Morphology.Disambiguator.DisambiguatorPrefixRule9 import DisambiguatorPrefixRule9
from Sastrawi.Morphology.Disambiguator.DisambiguatorPrefixRule10 import DisambiguatorPrefixRule10
from Sastrawi.Morphology.Disambiguator.DisambiguatorPrefixRule11 import DisambiguatorPrefixRule11
from Sastrawi.Morphology.Disambiguator.DisambiguatorPrefixRule12 import DisambiguatorPrefixRule12
from Sastrawi.Morphology.Disambiguator.DisambiguatorPrefixRule13a import DisambiguatorPrefixRule13a
from Sastrawi.Morphology.Disambiguator.DisambiguatorPrefixRule13b import DisambiguatorPrefixRule13b
from Sastrawi.Morphology.Disambiguator.DisambiguatorPrefixRule14 import DisambiguatorPrefixRule14

class VisitorProvider(object):
    """description of class"""

    def __init__(self):
        self.visitors = []
        self.suffixVisitors = []
        self.prefixVisitors = []

        self.initVisitors()

    def initVisitors(self):
        self.visitors.append(DontStemShortWord())

        #{lah|kah|tah|pun}
        self.suffixVisitors.append(RemoveInflectionalParticle())
        #{ku|mu|nya}
        self.suffixVisitors.append(RemoveInflectionalPossessivePronoun())
        #{i|kan|an}
        self.suffixVisitors.append(RemoveDerivationalSuffix())

        #{di|ke|se}
        self.prefixVisitors.append(RemovePlainPrefix())

        self.prefixVisitors.append(PrefixDisambiguator([DisambiguatorPrefixRule1a(), DisambiguatorPrefixRule1b()]))
        self.prefixVisitors.append(PrefixDisambiguator([DisambiguatorPrefixRule2()]))
        self.prefixVisitors.append(PrefixDisambiguator([DisambiguatorPrefixRule3()]))
        self.prefixVisitors.append(PrefixDisambiguator([DisambiguatorPrefixRule4()]))
        self.prefixVisitors.append(PrefixDisambiguator([DisambiguatorPrefixRule5()]))
        self.prefixVisitors.append(PrefixDisambiguator([DisambiguatorPrefixRule6a(), DisambiguatorPrefixRule6b()]))
        self.prefixVisitors.append(PrefixDisambiguator([DisambiguatorPrefixRule7()]))
        self.prefixVisitors.append(PrefixDisambiguator([DisambiguatorPrefixRule8()]))
        self.prefixVisitors.append(PrefixDisambiguator([DisambiguatorPrefixRule9()]))
        self.prefixVisitors.append(PrefixDisambiguator([DisambiguatorPrefixRule10()]))
        self.prefixVisitors.append(PrefixDisambiguator([DisambiguatorPrefixRule11()]))
        self.prefixVisitors.append(PrefixDisambiguator([DisambiguatorPrefixRule12()]))
        self.prefixVisitors.append(PrefixDisambiguator([DisambiguatorPrefixRule13a(), DisambiguatorPrefixRule13b()]))
        self.prefixVisitors.append(PrefixDisambiguator([DisambiguatorPrefixRule14()]))
        #self.prefixVisitors.append(PrefixDisambiguator([DisambiguatorPrefixRule15a(), DisambiguatorPrefixRule15b()]))
        #self.prefixVisitors.append(PrefixDisambiguator([DisambiguatorPrefixRule16()]))

        #disambiguators17 = [DisambiguatorPrefixRule17a(), DisambiguatorPrefixRule17b(), \
        #    DisambiguatorPrefixRule17c(), DisambiguatorPrefixRule17d()]
        #self.prefixVisitors.append(PrefixDisambiguator(disambiguators17))

        #self.prefixVisitors.append(PrefixDisambiguator([DisambiguatorPrefixRule18a(), DisambiguatorPrefixRule18b()]))
        #self.prefixVisitors.append(PrefixDisambiguator([DisambiguatorPrefixRule19()]))
        #self.prefixVisitors.append(PrefixDisambiguator([DisambiguatorPrefixRule20()]))
        #self.prefixVisitors.append(PrefixDisambiguator([DisambiguatorPrefixRule21a(), DisambiguatorPrefixRule21b()]))
        #self.prefixVisitors.append(PrefixDisambiguator([DisambiguatorPrefixRule23()]))
        #self.prefixVisitors.append(PrefixDisambiguator([DisambiguatorPrefixRule24()]))
        #self.prefixVisitors.append(PrefixDisambiguator([DisambiguatorPrefixRule25()]))
        #self.prefixVisitors.append(PrefixDisambiguator([DisambiguatorPrefixRule26a(), DisambiguatorPrefixRule26b()]))
        #self.prefixVisitors.append(PrefixDisambiguator([DisambiguatorPrefixRule27()]))
        #self.prefixVisitors.append(PrefixDisambiguator([DisambiguatorPrefixRule28a(), DisambiguatorPrefixRule28b()]))
        #self.prefixVisitors.append(PrefixDisambiguator([DisambiguatorPrefixRule29()]))

        #disambiguators30 = [DisambiguatorPrefixRule30a(), DisambiguatorPrefixRule30b(), \
        #    DisambiguatorPrefixRule30c()]
        #self.prefixVisitors.append(PrefixDisambiguator(disambiguators30))

        #self.prefixVisitors.append(PrefixDisambiguator([DisambiguatorPrefixRule31a(), DisambiguatorPrefixRule31b()]))
        #self.prefixVisitors.append(PrefixDisambiguator([DisambiguatorPrefixRule32()]))
        #self.prefixVisitors.append(PrefixDisambiguator([DisambiguatorPrefixRule34()]))

        ##CS additional rules
        #self.prefixVisitors.append(PrefixDisambiguator([DisambiguatorPrefixRule35()]))
        #self.prefixVisitors.append(PrefixDisambiguator([DisambiguatorPrefixRule36()]))

        ##CS infix rules
        #self.prefixVisitors.append(PrefixDisambiguator([DisambiguatorPrefixRule37a(), DisambiguatorPrefixRule37b()]))
        #self.prefixVisitors.append(PrefixDisambiguator([DisambiguatorPrefixRule38a(), DisambiguatorPrefixRule38b()]))
        #self.prefixVisitors.append(PrefixDisambiguator([DisambiguatorPrefixRule39a(), DisambiguatorPrefixRule39b()]))
        #self.prefixVisitors.append(PrefixDisambiguator([DisambiguatorPrefixRule40a(), DisambiguatorPrefixRule10b()]))

        ##Sastrawi rules
        ##ku-A, kau-A
        #self.prefixVisitors.append(PrefixDisambiguator([DisambiguatorPrefixRule41()]))
        #self.prefixVisitors.append(PrefixDisambiguator([DisambiguatorPrefixRule42()]))

    def getVisitors(self):
        return self.visitors

    def getSuffixVisitors(self):
        return self.suffixVisitors

    def getPrefixVisitors(self):
        return self.prefixVisitors

