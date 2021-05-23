import unittest
from selenium import webdriver

class Assertion(unittest.TestCase):
    def test1(self):
        driver = webdriver.Chrome("C:\Webdrivers\chromedriver_win32\chromedriver")

        #Verify if the driver veriable contains some value or not
        #self.assertIsNone(driver)
        self.assertIsNotNone(driver)

if __name__ == "__main__":
    unittest.main()