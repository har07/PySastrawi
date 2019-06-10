import unittest
from Sastrawi.stemmer import Stemmer

class Test_StemmerTest(unittest.TestCase):
    def setUp(self):
        self.stemmer = Stemmer(stopwords = ('di', 'ke'))

    def test_removeStopWord(self):
        self.assertEquals('pergi sekolah', self.stemmer.remove('pergi ke sekolah'))
        self.assertEquals('makan rumah', self.stemmer.remove('makan di rumah'))

if __name__ == '__main__':
    unittest.main()
