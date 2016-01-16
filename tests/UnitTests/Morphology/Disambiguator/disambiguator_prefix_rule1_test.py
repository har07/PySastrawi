import unittest
from Sastrawi.Morphology.Disambiguator.DisambiguatorPrefixRule1 import DisambiguatorPrefixRule1a, DisambiguatorPrefixRule1b

class Test_DisambiguatorPrefixRule1Test(unittest.TestCase):
    def setUp(self):
        self.subject1a = DisambiguatorPrefixRule1a()
        self.subject1b = DisambiguatorPrefixRule1b()
        return super(Test_DisambiguatorPrefixRule1Test, self).setUp()

    def test_disambiguate1a(self):
        self.assertEquals('ia-ia', self.subject1a.disambiguate('beria-ia'))
        self.assertIsNone(self.subject1a.disambiguate('berlari'))

    def test_disambiguate1b(self):
        self.assertEquals('rakit', self.subject1b.disambiguate('berakit'))
        self.assertIsNone(self.subject1b.disambiguate('bertabur'))

if __name__ == '__main__':
    unittest.main()
