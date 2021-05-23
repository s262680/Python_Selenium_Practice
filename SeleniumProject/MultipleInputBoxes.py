from selenium import webdriver

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome("C:\Webdrivers\chromedriver_win32\chromedriver")

driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")

#find elements with the "text_field" class name and store it in inputBoxes variable
inputBoxes=driver.find_elements(By.CLASS_NAME, "text_field")

#return length of the inputBoxes array
print(len(inputBoxes))

inputBoxes[0].send_keys("first")
inputBoxes[1].send_keys("last")
inputBoxes[2].send_keys("0747568315")

