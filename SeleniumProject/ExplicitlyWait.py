from selenium import webdriver

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome("C:\Webdrivers\chromedriver_win32\chromedriver")

driver.maximize_window()

driver.get("http://www.expedia.com")

ele=driver.find_element_by_xpath("//*[@id='uitk-tabs-button-container']/li[2]/a")
ele.click()

time.sleep(2)

ele=driver.find_element_by_xpath("//*[@id='location-field-leg1-origin-menu']/div[1]/button")
ele.click()

ele=driver.find_element_by_id("location-field-leg1-origin")
ele.send_keys("SFO")
ele.send_keys(Keys.ENTER)

ele=driver.find_element_by_xpath("//*[@id='location-field-leg1-destination-menu']/div[1]/button")
ele.click()

ele=driver.find_element_by_id("location-field-leg1-destination")
ele.send_keys("NYC")
ele.send_keys(Keys.ENTER)

ele=driver.find_element_by_xpath("//*[@id='wizard-flight-pwa-1']/div[3]/div[2]/button")
ele.click()

#create explicit wait with a maximum waiting time of 10 secs
wait=WebDriverWait(driver, 10)

#wait until the expected condition is met (element is visable), then store the element found into a veriable
ele=wait.until(EC.presence_of_element_located((By.ID, "stops-0")))
ele.click()



