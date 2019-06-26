import unittest
from Sastrawi import Stemmer

class Test_StemmerTest(unittest.TestCase):
    def setUp(self):
        self.stemmer = Stemmer(stopwords = ('di', 'ke'))

    def test_removeStopWord(self):
        self.assertEqual('pergi sekolah', self.stemmer.remove_stopword('pergi ke sekolah'))
        self.assertEqual('makan rumah', self.stemmer.remove_stopword('makan di rumah'))

if __name__ == '__main__':
    unittest.main()
