import unittest
from selenium import webdriver

class SearchEngineTest(unittest.TestCase):
    def test_Google(self):
        # self is an object that only belongs to this method
        self.driver=webdriver.Chrome(executable_path="C:\Webdrivers\chromedriver_win32\chromedriver")
        self.driver.get("http://www.google.com/")
        print("Title of the page is: "+self.driver.title)
        self.driver.close()

    def test_Bing(self):
        self.driver = webdriver.Chrome(executable_path="C:\Webdrivers\chromedriver_win32\chromedriver")
        self.driver.get("http://www.bing.com/")
        print("Title of the page is: " + self.driver.title)
        self.driver.close()

if __name__=="__main__":
    unittest.main()
