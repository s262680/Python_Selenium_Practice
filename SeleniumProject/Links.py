from selenium import webdriver

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome("C:\Webdrivers\chromedriver_win32\chromedriver")

driver.get("http://practice.automationtesting.in/shop/")

driver.maximize_window()

#find all the links in the page by using seach tag
links=driver.find_elements(By.TAG_NAME, "a")

print(len(links))

#print all the link texts by using for loop
for x in range(0, len(links)):
    print(links[x].text)

#locate and click on the link with partial link text "Functi", using explicit wait to wait for the element to appear on the page first
wait=WebDriverWait(driver, 10)
ele=wait.until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "Functi")))
ele.click()

#driver.find_element(By.PARTIAL_LINK_TEXT, "Functio").click()