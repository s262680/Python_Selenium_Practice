from selenium import webdriver

import time
#from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome("C:\Webdrivers\chromedriver_win32\chromedriver")

#stop further execution for a specific time
browser.implicitly_wait(5)

#opening URL takes some time
browser.get("http://practice.automationtesting.in/")

#assert is a function that used for debug, it will give a error msg when the condition is false and stop futher execution
assert "Automation Practice Site" in browser.title

#find the drop down menu by id
ele=browser.find_element_by_id("menu-icon")
ele.click()

#find the URL button
ele = browser.find_element_by_link_text("My Account")
ele.click()


ele = browser.find_element_by_name("username")
ele.send_keys("abc")
ele = browser.find_element_by_name("password")
ele.send_keys("abc")

time.sleep(5)

browser.quit()

