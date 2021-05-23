from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome("C:\Webdrivers\chromedriver_win32\chromedriver")

driver.get("http://testautomationpractice.blogspot.com/")

driver.maximize_window()

button=driver.find_element(By.XPATH, "//*[@id='HTML10']/div[1]/button")

actions=ActionChains(driver)

#perform double click
actions.double_click(button).perform()

#perform right click
actions.context_click(button).perform()
