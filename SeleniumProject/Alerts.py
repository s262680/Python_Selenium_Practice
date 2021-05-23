from selenium import webdriver
import time

driver = webdriver.Chrome("C:\Webdrivers\chromedriver_win32\chromedriver")
driver.get("http://testautomationpractice.blogspot.com/")

#Open the alert pop up
driver.find_element_by_xpath("//*[@id='HTML9']/div[1]/button").click()

time.sleep(2)

#Select OK on the alert pop up
#driver.switch_to.alert.accept()

#Select Cancel on the alert pop up
driver.switch_to.alert.dismiss()