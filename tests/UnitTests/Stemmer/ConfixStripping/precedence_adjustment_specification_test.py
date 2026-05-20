import unittest
from Sastrawi.Stemmer.ConfixStripping.PrecedenceAdjustmentSpecification import PrecedenceAdjustmentSpecification


class TestPrecedenceAdjustmentSpecification(unittest.TestCase):
    def setUp(self):
        self.spec = PrecedenceAdjustmentSpecification()

    def test_be_lah_rule(self):
        self.assertTrue(self.spec.is_satisfied_by('belajarlah'))

    def test_be_an_rule(self):
        self.assertTrue(self.spec.is_satisfied_by('belajaran'))

    def test_me_i_rule(self):
        self.assertTrue(self.spec.is_satisfied_by('mencintai'))

    def test_di_i_rule(self):
        self.assertTrue(self.spec.is_satisfied_by('dicintai'))

    def test_pe_i_rule(self):
        self.assertTrue(self.spec.is_satisfied_by('pencintai'))

    def test_ter_i_rule(self):
        self.assertTrue(self.spec.is_satisfied_by('tercintai'))

    def test_not_satisfied(self):
        self.assertFalse(self.spec.is_satisfied_by('makan'))
        self.assertFalse(self.spec.is_satisfied_by('minum'))
        self.assertFalse(self.spec.is_satisfied_by('bekerja'))
        self.assertFalse(self.spec.is_satisfied_by('menyuarakan'))


if __name__ == '__main__':
    unittest.main()
