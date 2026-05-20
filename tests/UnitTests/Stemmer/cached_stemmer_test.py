import unittest
from Sastrawi.Dictionary.ArrayDictionary import ArrayDictionary
from Sastrawi.Stemmer.Stemmer import Stemmer


class TestCachedStemmer(unittest.TestCase):
    def setUp(self):
        dictionary = ArrayDictionary(['jalan', 'makan', 'minum', 'tidur'])
        stemmer = Stemmer(dictionary)
        self.stemmer = stemmer

    def test_stem_single_word_in_dictionary(self):
        self.assertEqual('jalan', self.stemmer.stem('jalan'))

    def test_stem_sentence(self):
        result = self.stemmer.stem('saya mau makan dan minum')
        self.assertEqual('saya mau makan dan minum', result)

    def test_stem_plural_word(self):
        dictionary = ArrayDictionary(['buku'])
        stemmer = Stemmer(dictionary)
        self.assertEqual('buku', stemmer.stem('buku-buku'))

    def test_stem_word_not_in_dict(self):
        self.assertEqual('xyz', self.stemmer.stem('xyz'))

    def test_stem_empty_string(self):
        self.assertEqual('', self.stemmer.stem(''))

    def test_get_dictionary(self):
        d = self.stemmer.get_dictionary()
        self.assertIsNotNone(d)
        self.assertTrue(d.contains('jalan'))

    def test_is_plural_true(self):
        self.assertTrue(self.stemmer.is_plural('buku-buku'))

    def test_is_plural_false(self):
        self.assertFalse(self.stemmer.is_plural('buku'))

    def test_is_plural_ku_mu_nya_suffix_not_plural(self):
        self.assertFalse(self.stemmer.is_plural('mainku'))

    def test_is_plural_dash_with_suffix(self):
        self.assertTrue(self.stemmer.is_plural('malaikat-malaikat-Nya'))

    def test_stem_plural_identical_roots(self):
        dictionary = ArrayDictionary(['buku'])
        stemmer = Stemmer(dictionary)
        self.assertEqual('buku', stemmer.stem_word('buku-buku'))

    def test_stem_plural_different_roots(self):
        dictionary = ArrayDictionary(['bolak', 'balik'])
        stemmer = Stemmer(dictionary)
        self.assertEqual('bolak-balik', stemmer.stem_word('bolak-balik'))


if __name__ == '__main__':
    unittest.main()
