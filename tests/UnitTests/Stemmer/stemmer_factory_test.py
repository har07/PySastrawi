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

    # Test Waktu Stemming < 3 detik
    # @author Mufid Jamaluddin
    def test_execution_time(self):
        start = time.time()
        sentence  = 'Rakyat memenuHi halaMan geDung DPR unTuk menyuarakan isi hatinya. Saat Itu, situasi sangat genting sekali. Terjadi kerusuhan yang mengiringi pergerakan mahasiswa yang memperjuangkan reformasi.'

        factory = StemmerFactory()
        stemmer = factory.create_stemmer()
        stemmer.stem(sentence)

        end = time.time()

        execution_time = end - start
        self.assertTrue(execution_time < 3)

    def test_getWordsFromFile(self):
        factory = StemmerFactory()
        factory.get_words_from_file()

    # Test Stemming per Kata
    # @author Mufid Jamaluddin
    def test_word_stemming(self):
        factory = StemmerFactory()
        stemmer = factory.create_stemmer()
        self.assertEqual('besar', stemmer.stem('terbesar'))
        self.assertEqual('abai', stemmer.stem('diabaikan'))

    # Test Stemming dengan isDev=True (No Cache)
    # @author Mufid Jamaluddin
    def test_word_stemmingdev(self):
        factory = StemmerFactory()
        stemmer = factory.create_stemmer(isDev=True)
        self.assertEqual('besar', stemmer.stem('terbesar'))
        self.assertEqual('abai', stemmer.stem('diabaikan'))

    # Test Stemming dengan list tokens
    # @author Mufid Jamaluddin
    def test_tokens_stemming(self):
        factory = StemmerFactory()
        stemmer = factory.create_stemmer()
        tokens = ['perekonomian', '', 'indonesia', 'sedang', ' ', 'dalam', 'pertumbuhan' ,'yang', 'membanggakan']
        clean_tokens = stemmer.stem_tokens(tokens)
        self.assertEqual('ekonomi', clean_tokens[0])
        self.assertEqual('indonesia', clean_tokens[1])
        self.assertEqual('sedang', clean_tokens[2])
        self.assertEqual('dalam', clean_tokens[3])
        self.assertEqual('tumbuh', clean_tokens[4])
        self.assertEqual('yang', clean_tokens[5])
        self.assertEqual('bangga', clean_tokens[6])

if __name__ == '__main__':
    unittest.main()
