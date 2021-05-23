from selenium import webdriver

from selenium.webdriver.common.keys import Keys

#import time package to use the time fuction
import time

#create driver for chrome browser
driver=webdriver.Chrome(executable_path="C:\Webdrivers\chromedriver_win32\chromedriver")

#access the web page
driver.get("http://demo.automationtesting.in/Windows.html")

#return title of the web page
print(driver.title)

#return URL of the web page
print(driver.current_url)

#Must replace the double quotation with single quotation within the xpath
driver.find_element_by_xpath("//*[@id='Tabbed']/a/button").click()

#wait for 5 secs
time.sleep(5)

#close a single page
#driver.close()

#close all pages
driver.quit()