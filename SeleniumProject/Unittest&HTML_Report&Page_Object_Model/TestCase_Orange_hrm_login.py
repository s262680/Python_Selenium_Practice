from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
import HtmlTestRunner

class OrangeHRMTest(unittest.TestCase):

    # A setupClass method will be executed once when the class started
    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Chrome(executable_path="C:\Webdrivers\chromedriver_win32\chromedriver")
        cls.driver.maximize_window()

    # Fail this TC intentionally to see the fail result in the report
    def test_homePageTitle(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com")
        self.assertEqual("OrangeHRM123", self.driver.title, "webpage title is not matching")

    def test_login(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com")
        self.driver.find_element(By.ID, "txtUsername").send_keys("Admin")
        self.driver.find_element(By.ID, "txtPassword").send_keys("admin123")
        self.driver.find_element(By.ID, "btnLogin").click()
        self.assertEqual("OrangeHRM", self.driver.title, "webpage title is not matching")

    # A tearDownClass method will be executed once after the class completed
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        print("Test completed...")

#generate a html report inside the Reports folder of the current dir
if __name__=="__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="..\\Unittest&HTML_Report&Page_Object_Model\\Reports"))

#Must run with with Python to generate the report