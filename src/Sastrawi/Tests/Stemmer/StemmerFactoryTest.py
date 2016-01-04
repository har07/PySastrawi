import unittest
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory

class Test_StemmerFactoryTest(unittest.TestCase):
    def test_fungsional(self):
        factory = StemmerFactory()
        stemmer = factory.createStemmer()

        sentence = 'Perekonomian Indonesia sedang dalam pertumbuhan yang membanggakan. beterbangan'
        output = stemmer.stem(sentence)

        if output == sentence:
            raise AssertionError('input sentence was not stemmed at all')

    def test_getWordsFromFile(self):
        factory = StemmerFactory()
        factory.getWordsFromFile()

if __name__ == '__main__':
    unittest.main()
