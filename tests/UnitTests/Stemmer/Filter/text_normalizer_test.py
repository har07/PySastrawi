import unittest
from Sastrawi.Stemmer.Filter.TextNormalizer import normalize_text


class TestTextNormalizer(unittest.TestCase):
    def test_lowercase(self):
        self.assertEqual('abcd', normalize_text('ABCD'))
        self.assertEqual('abcd', normalize_text('AbCd'))

    def test_remove_punctuation(self):
        self.assertEqual('abc', normalize_text('abc!'))
        self.assertEqual('abc', normalize_text('abc.'))
        self.assertEqual('a b c', normalize_text('a,b,c'))
        self.assertEqual('a b c', normalize_text('a.b.c'))
        self.assertEqual('a1 b2', normalize_text('a1!b2'))
        self.assertEqual('abc', normalize_text('"abc"'))

    def test_collapse_multiple_spaces(self):
        self.assertEqual('a b', normalize_text('a   b'))
        self.assertEqual('a b', normalize_text('a    b'))
        self.assertEqual('a b c', normalize_text('a  b   c'))

    def test_newlines_and_tabs(self):
        self.assertEqual('a b', normalize_text('a\nb'))
        self.assertEqual('a b', normalize_text('a\r\nb'))
        self.assertEqual('a b', normalize_text('a\tb'))

    def test_empty_string(self):
        self.assertEqual('', normalize_text(''))

    def test_only_punctuation(self):
        self.assertEqual('', normalize_text('!@#$%'))


if __name__ == '__main__':
    unittest.main()
