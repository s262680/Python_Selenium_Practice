from selenium import webdriver

driver = webdriver.Chrome("C:\Webdrivers\chromedriver_win32\chromedriver")

driver.get("https://www.amazon.co.uk/")


#Capture all cookies created by the browser
cookies=driver.get_cookies()
print(len(cookies))
print(cookies)

#Adding new cookie to the browser
cookie={"name":"MyCookie", "value":"123456"}
driver.add_cookie(cookie)

#Capture all cookies again after adding new cookie
cookies=driver.get_cookies()
print(len(cookies))
print(cookies)

#Deleting cookie
driver.delete_cookie("MyCookie")

#Capture all cookies again after deleting the cookie
cookies=driver.get_cookies()
print(len(cookies))
print(cookies)

#Capture all cookies again after deleting all cookies
driver.delete_all_cookies()
cookies=driver.get_cookies()
print(len(cookies))
print(cookies)