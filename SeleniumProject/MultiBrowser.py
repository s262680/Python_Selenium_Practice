from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#create driver for chrome browser
Driver=webdriver.Chrome(executable_path="C:\Webdrivers\chromedriver_win32\chromedriver.exe")

#create driver for firefox browser
#Driver=webdriver.Firefox(executable_path="C:\Webdrivers\geckodriver-v0.29.1-win64\geckodriver.exe")

#access the web page
Driver.get("http://google.com/")

#return title of the web page
print(Driver.title)

#return URL of the web page
print(Driver.current_url)

#return HTML code of the web page
#print(Driver.page_source)

#close the brower
Driver.close()