from selenium import webdriver

from selenium.webdriver.common.keys import Keys

import time

driver=webdriver.Chrome("C:\Webdrivers\chromedriver_win32\chromedriver")

#open first page
driver.get("http://demo.automationtesting.in/Windows.html")

time.sleep(3)
print(driver.title)

#replace the first page with another page
driver.get("http://google.com")

time.sleep(3)
print(driver.title)

#go back to the previous page
driver.back()


time.sleep(3)
print(driver.title)
#go back to the other page
driver.forward()

time.sleep(3)
print(driver.title)

driver.quit()