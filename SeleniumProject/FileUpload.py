from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome("C:\Webdrivers\chromedriver_win32\chromedriver")

driver.get("http://testautomationpractice.blogspot.com/")

driver.maximize_window()

#upload button is located in a frame, switch to it before searching for the upload button
driver.switch_to.frame(0)

#store the file path in a variable, note that all the backward slashs have to be replaced with forward slashs
fileLocation="C://Users/K/Downloads/emptyTF.txt"

#locate the button and send the path to it in order to upload the file
driver.find_element(By.ID, "RESULT_FileUpload-10").send_keys(fileLocation)