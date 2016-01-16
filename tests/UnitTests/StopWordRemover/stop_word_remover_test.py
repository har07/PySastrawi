import unittest
from Sastrawi.Dictionary.ArrayDictionary import ArrayDictionary
from Sastrawi.StopWordRemover.StopWordRemover import StopWordRemover

class Test_StopWordRemoverTest(unittest.TestCase):
    def setUp(self):
        self.dictionary = ArrayDictionary(['di', 'ke'])
        self.stopWordRemover = StopWordRemover(self.dictionary)
        return super(Test_StopWordRemoverTest, self).setUp()

    def test_getDictionaryPreserveInstance(self):
        self.assertEqual(self.dictionary, self.stopWordRemover.get_dictionary())

    def test_removeStopWord(self):
        self.assertEquals('pergi sekolah', self.stopWordRemover.remove('pergi ke sekolah'))
        self.assertEquals('makan rumah', self.stopWordRemover.remove('makan di rumah'))

if __name__ == '__main__':
    unittest.main()
