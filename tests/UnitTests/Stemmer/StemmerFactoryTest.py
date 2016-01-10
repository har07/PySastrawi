import unittest
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from Sastrawi.Stemmer.Stemmer import Stemmer

class Test_StemmerFactoryTest(unittest.TestCase):
    def setUp(self):
        self.factory = StemmerFactory()
        return super(Test_StemmerFactoryTest, self).setUp()

    def test_createStemmerReturnStemmer(self):
        stemmer = self.factory.createStemmer()
        self.assertIsNotNone(stemmer)
        #self.assertIsInstance(stemmer, Stemmer)

    def test_fungsional(self):
        factory = StemmerFactory()
        stemmer = factory.createStemmer()

        sentence = 'malaikat-malaikat-Nya'
        expected = 'malaikat'
        output = stemmer.stem(sentence)

        if output != expected:
            raise AssertionError(str.format('output is {} instead of {}', output, expected))

    def test_getWordsFromFile(self):
        factory = StemmerFactory()
        factory.getWordsFromFile()

if __name__ == '__main__':
    unittest.main()
