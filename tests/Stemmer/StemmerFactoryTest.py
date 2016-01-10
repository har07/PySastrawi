import unittest
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory

class Test_StemmerFactoryTest(unittest.TestCase):
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
