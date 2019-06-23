import unittest
from Sastrawi.rules import isIAPS

class Test_isIAPSTest(unittest.TestCase):
    def setUp(self):
        self.isIAPS = isIAPS
        return super(Test_isIAPSTest, self).setUp()

    def test_containsInvalidAffixPair(self):
        self.assertFalse(self.isIAPS('memberikan'))
        self.assertFalse(self.isIAPS('ketahui'))

        self.assertTrue(self.isIAPS('berjatuhi'))
        self.assertTrue(self.isIAPS('dipukulan'))
        self.assertTrue(self.isIAPS('ketiduri'))
        self.assertTrue(self.isIAPS('ketidurkan'))
        self.assertTrue(self.isIAPS('menduaan'))
        self.assertTrue(self.isIAPS('terduaan'))
        self.assertTrue(self.isIAPS('perkataan'))

if __name__ == '__main__':
    unittest.main()
