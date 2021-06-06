import unittest
import HtmlTestRunner
from selenium import webdriver
from SeleniumProject.Unittest_HTMLreports_PageObjectModel.POM.PageObjects.LoginPage import LoginPage
import time

#require if we want to run the project through command prompt
#import sys
#sys.path.append("C://Users//K//PycharmProjects//Python_Selenium_Practice")

class LoginTest(unittest.TestCase):
    #variables
    URL="https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F"
    username="admin@yourstore.com"
    password="admin"
    driver = webdriver.Chrome(executable_path="..\\Driver\\chromedriver.exe")

    @classmethod
    def setUpClass(cls):
        cls.driver.get(cls.URL)
        cls.driver.maximize_window()

    def test_login(self):
        #create an object for loginpage class
        lp=LoginPage(self.driver)

        #excute methods from loginpage class
        lp.clearUserName(self.username)
        lp.clearPassword(self.password)
        lp.setUserName(self.username)
        lp.setPassword(self.password)
        lp.clickLogin()
        time.sleep(3)
        self.assertEqual("Dashboard / nopCommerce administration", self.driver.title, "Webpage title does not match")

    @classmethod
    def tearDown(cls):
        cls.driver.quit()

if __name__=="__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="..\\Reports"))