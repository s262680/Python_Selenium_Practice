import unittest
from selenium import webdriver

class Assertion(unittest.TestCase):
    def test1(self):
        driver = webdriver.Chrome("C:\Webdrivers\chromedriver_win32\chromedriver")
        driver.get("https://www.google.com/")
        titleOfWebpage=driver.title

        #Verify if the "titleOfWebpage" is equal to "Google", if not then display an error message
        self.assertEqual("Google123",titleOfWebpage,"Webpage titles are not same")
        #self.assertNotEqual("Google",titleOfWebpage,"Webpage titles are same")

if __name__=="__main__":
    unittest.main()