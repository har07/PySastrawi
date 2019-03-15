import unittest
import time
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory
from Sastrawi.StopWordRemover.StopWordRemover import StopWordRemover

class Test_StopWordRemoverFactoryTest(unittest.TestCase):
    def setUp(self):
        self.factory = StopWordRemoverFactory()
        return super(Test_StopWordRemoverFactoryTest, self).setUp()

    def test_createStopWordRemover(self):
        self.assertIsInstance(self.factory.create_stop_word_remover(), StopWordRemover)
    
    def test_stopwordRemoval(self):
        sremover = self.factory.create_stop_word_remover()
        self.assertEqual('pergi sekolah', sremover.remove('pergi ke sekolah yang'))
        self.assertEqual('makan rumah', sremover.remove('makan di rumah yang'))
    
    def test_tokens_stopwordRemoval(self):
        tokens = ['pergi', 'ke', 'sekolah', 'yang', 'bagus', 'adalah', 'impian']
        sremover = self.factory.create_stop_word_remover()
        clean_tokens = sremover.remove_tokens(tokens)
        text = ' '.join(clean_tokens)
        self.assertEquals('pergi sekolah bagus impian', text)
        self.assertEqual('pergi', clean_tokens[0])
        self.assertEqual('sekolah', clean_tokens[1])
        self.assertEqual('bagus', clean_tokens[2])
        self.assertEqual('impian', clean_tokens[3])

    def test_execution_time(self):
        start = time.time()
        sentence  = 'Rakyat memenuHi halaMan geDung DPR unTuk menyuarakan isi hatinya. Saat Itu, situasi sangat genting sekali. Terjadi kerusuhan yang mengiringi pergerakan mahasiswa yang memperjuangkan reformasi.'
        sremover = self.factory.create_stop_word_remover()
        sremover.remove(sentence)
        end = time.time()
        # print(execution_time)
        execution_time = end - start

        self.assertTrue(execution_time < 1)

if __name__ == '__main__':
    unittest.main()
