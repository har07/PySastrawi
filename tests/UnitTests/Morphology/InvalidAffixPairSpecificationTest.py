import unittest
from Sastrawi.Morphology.InvalidAffixPairSpecification import InvalidAffixPairSpecification

class Test_InvalidAffixPairSpecificationTest(unittest.TestCase):
    def setUp(self):
        self.specification = InvalidAffixPairSpecification()
        return super(Test_InvalidAffixPairSpecificationTest, self).setUp()

    def test_containsInvalidAffixPair(self):
        self.assertFalse(self.specification.is_satisfied_by('memberikan'))
        self.assertFalse(self.specification.is_satisfied_by('ketahui'))

        self.assertTrue(self.specification.is_satisfied_by('berjatuhi'))
        self.assertTrue(self.specification.is_satisfied_by('dipukulan'))
        self.assertTrue(self.specification.is_satisfied_by('ketiduri'))
        self.assertTrue(self.specification.is_satisfied_by('ketidurkan'))
        self.assertTrue(self.specification.is_satisfied_by('menduaan'))
        self.assertTrue(self.specification.is_satisfied_by('terduaan'))
        self.assertTrue(self.specification.is_satisfied_by('perkataan'))

if __name__ == '__main__':
    unittest.main()
