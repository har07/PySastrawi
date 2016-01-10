import unittest
from Sastrawi.Dictionary.ArrayDictionary import ArrayDictionary
from Sastrawi.Dictionary.DictionaryInterface import DictionaryInterface

class Test_ArrayDictionaryTest(unittest.TestCase):
    def setUp(self):
        self.dictionary = ArrayDictionary()
        return super(Test_ArrayDictionaryTest, self).setUp()

    def test_addAndContain(self):
        self.assertFalse(self.dictionary.contains('word'))
        self.dictionary.add('word')
        self.assertTrue(self.dictionary.contains('word'))

    def test_addCountWord(self):
        self.assertEquals(0, self.dictionary.count())
        self.dictionary.add('word')
        self.assertEquals(1, self.dictionary.count())

    def test_addWordIgnoreEmptyString(self):
        self.assertEquals(0, self.dictionary.count())
        self.dictionary.add('')
        self.assertEquals(0, self.dictionary.count())

    def test_addWords(self):
        words = ['word1', 'word2']
        self.dictionary.addWords(words)
        self.assertEquals(2, self.dictionary.count())
        self.assertTrue(self.dictionary.contains('word1'))
        self.assertTrue(self.dictionary.contains('word2'))

    def test_constructorPreserveWords(self):
        words = ['word1', 'word2']
        dictionary = ArrayDictionary(words)
        self.assertEquals(2, dictionary.count())
        self.assertTrue(dictionary.contains('word1'))
        self.assertTrue(dictionary.contains('word2'))

if __name__ == '__main__':
    unittest.main()
