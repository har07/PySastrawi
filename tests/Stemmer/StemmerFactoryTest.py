import unittest
from Sastrawi.Stemmer import StemmerFactory

class Test_StemmerFactoryTest(unittest.TestCase):
    def test_getWordsFromFile(self):
        factory = StemmerFactory()
        factory.getWordsFromFile()

if __name__ == '__main__':
    unittest.main()
