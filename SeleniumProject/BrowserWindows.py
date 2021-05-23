from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time

driver = webdriver.Chrome("C:\Webdrivers\chromedriver_win32\chromedriver")

driver.get("https://www.selenium.dev/selenium/docs/api/java/index.html?overview-summary.html")

#open page in a new tab
driver.execute_script("window.open('https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407');")
driver.execute_script("window.open('https://google.com');")

#handle of the parent window handle value
print(driver.current_window_handle)

#return all the handle values of opened browser windows and store it into a variable
handles=(driver.window_handles)

#loop through all the browser windows and print their titles, if the title is equal to "Google" then it will close the tab
for handle in handles:
    driver.switch_to.window(handle)
    print(driver.title)
    if driver.title=="Google":
        driver.close()

#return all the handle values of current opened browser windows
handles=(driver.window_handles)

#switch between tabs
driver.switch_to.window(handles[0])
time.sleep(2)
driver.switch_to.window(handles[1])
time.sleep(2)
driver.switch_to.window(handles[0])
