import unittest
import time
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from Sastrawi.Stemmer.Stemmer import Stemmer

class Test_StemmerFactoryTest(unittest.TestCase):
    def setUp(self):
        self.factory = StemmerFactory()
        return super(Test_StemmerFactoryTest, self).setUp()

    def test_createStemmerReturnStemmer(self):
        stemmer = self.factory.create_stemmer()
        self.assertIsNotNone(stemmer)
        #self.assertIsInstance(stemmer, Stemmer)

    def test_fungsional(self):
        factory = StemmerFactory()
        stemmer = factory.create_stemmer()

        sentence = 'malaikat-malaikat-Nya'
        expected = 'malaikat'
        output = stemmer.stem(sentence)

        if output != expected:
            raise AssertionError(str.format('output is {} instead of {}', output, expected))

    def test_execution_time(self):
        start = time.time()
        sentence  = 'Rakyat memenuHi halaMan geDung DPR unTuk menyuarakan isi hatinya. Saat Itu, situasi sangat genting sekali. Terjadi kerusuhan yang mengiringi pergerakan mahasiswa yang memperjuangkan reformasi.'

        factory = StemmerFactory()
        stemmer = factory.create_stemmer()

        stemmer.stem(sentence)

        end = time.time()

        execution_time = end - start

        # print(execution_time)

        # test execution time < 3 seconds
        self.assertTrue(execution_time < 3)

    def test_getWordsFromFile(self):
        factory = StemmerFactory()
        factory.get_words_from_file()

if __name__ == '__main__':
    unittest.main()
