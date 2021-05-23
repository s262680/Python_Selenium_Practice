import unittest

#Create a Test class object
class Test(unittest.TestCase):
    def test_firstTestCase(self): #for test method, the name must start with "test_"
        print("This is my first unit test case")

    def test_secondTestCase(self):
        print("This is my second unit test case")

#__name__ is a python default variable represent the current model name
if __name__=="__main__":
    unittest.main() #run all test cases