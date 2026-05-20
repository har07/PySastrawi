import unittest
from Sastrawi.Stemmer.Cache.ArrayCache import ArrayCache


class TestArrayCache(unittest.TestCase):
    def setUp(self):
        self.cache = ArrayCache()

    def test_has_returns_false_for_missing_key(self):
        self.assertFalse(self.cache.has('missing'))

    def test_set_and_has_and_get(self):
        self.cache.set('key', 'value')
        self.assertTrue(self.cache.has('key'))
        self.assertEqual('value', self.cache.get('key'))

    def test_get_returns_none_for_missing_key(self):
        self.assertIsNone(self.cache.get('missing'))

    def test_overwrite_value(self):
        self.cache.set('key', 'first')
        self.cache.set('key', 'second')
        self.assertEqual('second', self.cache.get('key'))

    def test_multiple_keys(self):
        self.cache.set('a', '1')
        self.cache.set('b', '2')
        self.assertTrue(self.cache.has('a'))
        self.assertTrue(self.cache.has('b'))
        self.assertEqual('1', self.cache.get('a'))
        self.assertEqual('2', self.cache.get('b'))


if __name__ == '__main__':
    unittest.main()
