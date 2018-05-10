import unittest

from Sastrawi.StopWordRemover.StopWordRemover import StopWordRemover
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory


class Test_StopWordRemoverFactoryTest(unittest.TestCase):
    def setUp(self):
        self.factory = StopWordRemoverFactory()
        return super(Test_StopWordRemoverFactoryTest, self).setUp()

    def test_createStopWordRemover(self):
        self.assertIsInstance(self.factory.create_stop_word_remover(), StopWordRemover)

    def test_appendStopwords(self):
        new_stopwords = ['dengan', 'ia', 'bahwa', 'oleh']
        self.factory.append_stop_words(new_stopwords)

        for sw in new_stopwords:
            self.assertIn(sw, self.factory.stopwords, "Failed to append {} to stopwords".format(sw))


if __name__ == '__main__':
    unittest.main()
