import unittest

# A setUpModule method will be executed before any class or method present in the test case class
def setUpModule():
    print("setUpModule")

# A tearDownModule method will be executed after completion of everything present in the test class
def tearDownModule():
    print("tearDownModule")


TC = unittest.TestCase

class AppTesting(TC):

    # A setup method will be executed before each method
    def setUp(self):
        print("This is login test")

    # A tearDown method will be executed after each method
    def tearDown(self):
        print("This is logout test")

    # A setupClass method will be executed once when the class started
    @classmethod
    def setUpClass(cls):
        print("Open Application")

    # A tearDownClass method will be executed once after the class completed
    @classmethod
    def tearDownClass(cls):
        print("Close Application")



    #methods

    def test_search(self):
        print("This is search test")

    def test_advancedSearch(self):
        print("This is advanced search test")

    def test_prepaidRecharge(self):
        print("This is prepaid recharge test")

    def test_postpaidRecharge(self):
        print("This is a post paid recharge test")

if __name__=="__main__":
    unittest.main()