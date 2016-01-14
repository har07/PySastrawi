import unittest
from Sastrawi.Dictionary.ArrayDictionary import ArrayDictionary
from Sastrawi.Stemmer.Stemmer import Stemmer

class Test_StemmerTest(unittest.TestCase):
    def setUp(self):
        self.dictionary = ArrayDictionary(['beri'])
        self.stemmer = Stemmer(self.dictionary)

    def test_StemmerImplementsStemmerInterface(self):
        self.assertIsInstance(self.stemmer, Stemmer)

    def test_StemReturnImmediatelyOnShortWord(self):
        """Don't stem such a short word (three or fewer characters)"""
        self.assertEquals('mei', self.stemmer.stem('mei'))
        self.assertEquals('bui', self.stemmer.stem('bui'))

    def test_StemReturnImmediatelyIfFoundOnDictionary(self):
        """To prevent overstemming : nilai could have been overstemmed to nila
        if we don't lookup against the dictionary
        """
        self.stemmer.get_dictionary().add('nila')
        self.assertEquals('nila', self.stemmer.stem('nilai'))
        self.stemmer.get_dictionary().add('nilai')
        self.assertEquals('nilai', self.stemmer.stem('nilai'))

if __name__ == '__main__':
    unittest.main()
