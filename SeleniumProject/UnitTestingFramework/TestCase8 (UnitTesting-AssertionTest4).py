import unittest

class Assertion(unittest.TestCase):
    def test1(self):
        list={"user", "password", "ID"}

        #verify if the value is present in the list or not
        #self.assertIn("password", list)
        self.assertNotIn("password123", list)

if __name__ == "__main__":
    unittest.main()