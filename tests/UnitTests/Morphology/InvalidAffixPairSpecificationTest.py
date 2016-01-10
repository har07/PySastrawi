import unittest
from Sastrawi.Morphology.InvalidAffixPairSpecification import InvalidAffixPairSpecification

class Test_InvalidAffixPairSpecificationTest(unittest.TestCase):
    def setUp(self):
        self.specification = InvalidAffixPairSpecification()
        return super(Test_InvalidAffixPairSpecificationTest, self).setUp()

    def test_containsInvalidAffixPair(self):
        self.assertFalse(self.specification.isSatisfiedBy('memberikan'))
        self.assertFalse(self.specification.isSatisfiedBy('ketahui'))

        self.assertTrue(self.specification.isSatisfiedBy('berjatuhi'))
        self.assertTrue(self.specification.isSatisfiedBy('dipukulan'))
        self.assertTrue(self.specification.isSatisfiedBy('ketiduri'))
        self.assertTrue(self.specification.isSatisfiedBy('ketidurkan'))
        self.assertTrue(self.specification.isSatisfiedBy('menduaan'))
        self.assertTrue(self.specification.isSatisfiedBy('terduaan'))
        self.assertTrue(self.specification.isSatisfiedBy('perkataan'))

if __name__ == '__main__':
    unittest.main()
