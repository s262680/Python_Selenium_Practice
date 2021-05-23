import unittest
from selenium import webdriver

class Assertion(unittest.TestCase):
    def test1(self):
        driver = webdriver.Chrome("C:\Webdrivers\chromedriver_win32\chromedriver")
        driver.get("https://www.google.com/")
        titleOfWebpage=driver.title

        #An assertion similar to if statment
        #self.assertTrue(titleOfWebpage == "Google123")
        self.assertFalse(titleOfWebpage == "Google123")


if __name__=="__main__":
    unittest.main()