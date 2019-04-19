import unittest
from Sastrawi.Dictionary.ArrayDictionary import ArrayDictionary
from Sastrawi.Dictionary.DictionaryInterface import DictionaryInterface

class Test_ArrayDictionaryTest(unittest.TestCase):
    def setUp(self):
        self.dictionary = ArrayDictionary()
        return super(Test_ArrayDictionaryTest, self).setUp()

    def test_add_and_contain(self):
        self.assertFalse(self.dictionary.contains('word'))
        self.dictionary.add('word')
        self.assertTrue(self.dictionary.contains('word'))

    def test_add_count_word(self):
        self.assertEquals(0, self.dictionary.count())
        self.dictionary.add('word')
        self.assertEquals(1, self.dictionary.count())

    def test_add_word_ignore_empty_string(self):
        self.assertEquals(0, self.dictionary.count())
        self.dictionary.add('')
        self.assertEquals(0, self.dictionary.count())

    def test_add_words(self):
        words = ['word1', 'word2']
        self.dictionary.add_words(words)
        self.assertEquals(2, self.dictionary.count())
        self.assertTrue(self.dictionary.contains('word1'))
        self.assertTrue(self.dictionary.contains('word2'))

    def test_constructor_preserve_words(self):
        words = ['word1', 'word2']
        dictionary = ArrayDictionary(words)
        self.assertEquals(2, dictionary.count())
        self.assertTrue(dictionary.contains('word1'))
        self.assertTrue(dictionary.contains('word2'))

    # Test ArrayDictionary dengan tipe data dict
    # @author Mufid Jamaluddin
    def test_dict_param(self):
        dictionary = ArrayDictionary({'word1':'word1', 'word2':'word2'})
        self.assertTrue(dictionary.contains('word1'))
        self.assertTrue(dictionary.contains('word2'))
        self.assertFalse(dictionary.contains('word3'))
        self.assertEqual(2, dictionary.count())
        dictionary.add('word3')
        dictionary.add(' ')
        self.assertTrue(dictionary.contains('word3'))
        self.assertEqual(3, dictionary.count())

    def test_non_dict_list(self):
        dictionary = ArrayDictionary('$$%&**&(^&')
        self.assertEqual(0, dictionary.count())

if __name__ == '__main__':
    unittest.main()
