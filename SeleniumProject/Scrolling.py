from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome("C:\Webdrivers\chromedriver_win32\chromedriver")

driver.get("http://testautomationpractice.blogspot.com/")

driver.maximize_window()

#scroll down the page by specified pixels
#driver.execute_script("window.scrollBy(0,500)","")

#scroll down until the element is visiable
element=driver.find_element(By.LINK_TEXT,"Posts (Atom)")
driver.execute_script("arguments[0].scrollIntoView();",element)

#scroll til the end of the page
#driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")

