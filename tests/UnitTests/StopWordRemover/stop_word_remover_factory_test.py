import unittest
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory
from Sastrawi.StopWordRemover.StopWordRemover import StopWordRemover

class Test_StopWordRemoverFactoryTest(unittest.TestCase):
    def setUp(self):
        self.factory = StopWordRemoverFactory()
        return super(Test_StopWordRemoverFactoryTest, self).setUp()

    def test_createStopWordRemover(self):
        self.assertIsInstance(self.factory.create_stop_word_remover(), StopWordRemover)

if __name__ == '__main__':
    unittest.main()
