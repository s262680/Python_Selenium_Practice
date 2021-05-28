import unittest

class PaymentTest(unittest.TestCase):
    def test_paymentInDollor(self):
        print("This is payment in dollor test")
        self.assertTrue(True)

    def test_paymentInGBP(self):
        print("This is payment in GBP test")
        self.assertTrue(True)

if __name__=="__main__":
    unittest.main()