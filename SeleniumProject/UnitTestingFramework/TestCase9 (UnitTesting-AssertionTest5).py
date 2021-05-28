import unittest

class Test(unittest.TestCase):
    def testName(self):
        #pass if first value greater than the second value
        #self.assertGreater(100,10)
        # pass if first value greater or equal to the second value
        #self.assertGreaterEqual(100, 100)
        #self.assertLess(10,200)
        self.assertLessEqual(10,100)

if __name__=="__main__":
    unittest.main()