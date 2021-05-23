import unittest

class SkippingTest(unittest.TestCase):

    #methods

    def test_search(self):
        print("This is search test")

    # decorator that allows skipping the 1 method below (appears to be outdated method?)
    @unittest.SkipTest
    def test_advancedSearch(self):
        print("This is advanced search test")

    # decorator that allows skipping the 1 method below and leave a message
    @unittest.skip("I am skipping this method because its not ready yet")
    def test_prepaidRecharge(self):
        print("This is prepaid recharge test")

    # skip if certain condition is met
    @unittest.skipIf(1!=2, "Number not equal")
    def test_postpaidRecharge(self):
        print("This is a post paid recharge test")

if __name__=="__main__":
    unittest.main()