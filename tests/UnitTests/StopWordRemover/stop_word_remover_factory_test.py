import unittest
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory
from Sastrawi.StopWordRemover.StopWordRemover import StopWordRemover

class TestStopWordRemoverFactory(unittest.TestCase):
    def setUp(self):
        self.factory = StopWordRemoverFactory()
        return super().setUp()

    def test_createStopWordRemover(self):
        self.assertIsInstance(self.factory.create_stop_word_remover(), StopWordRemover)

if __name__ == '__main__':
    unittest.main()
