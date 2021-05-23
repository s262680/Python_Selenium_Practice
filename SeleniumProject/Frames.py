from selenium import webdriver
from selenium.webdriver.common.by import By

import time

driver = webdriver.Chrome("C:\Webdrivers\chromedriver_win32\chromedriver")
driver.get("https://www.selenium.dev/selenium/docs/api/java/index.html?overview-summary.html")


#frames=driver.find_elements(By.TAG_NAME, "iframe")
#for x in range(0, len(frames)):
    #print(frames[x].text)

#switch to the first frame
driver.switch_to.frame("packageListFrame")

time.sleep(1)

#click on the link text in the first frame
ele=driver.find_element(By.LINK_TEXT, "org.openqa.selenium.chrome")
ele.click()

time.sleep(1)

#Must switch back to default content before jumping to another frame
driver.switch_to.default_content()

time.sleep(1)

driver.switch_to.frame("packageFrame")
ele=driver.find_element(By.LINK_TEXT, "ChromeDriverInfo")
ele.click()

time.sleep(1)

driver.switch_to.default_content()

time.sleep(1)

driver.switch_to.frame("classFrame")
ele=driver.find_element(By.LINK_TEXT, "org.openqa.selenium.chromium.ChromiumDriverInfo")
ele.click()