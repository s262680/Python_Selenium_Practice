from selenium import webdriver

from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome("C:\Webdrivers\chromedriver_win32\chromedriver")

driver.get("http://practice.automationtesting.in/my-account/")

#store the found element into ele variable
userEle=driver.find_element_by_name("username")

#reture true or false based on element status
print(userEle.is_displayed())
print(userEle.is_enabled())

#store the found element into ele variable
pwEle=driver.find_element_by_name("password")

#reture true or false based on element status
print(pwEle.is_displayed())
print(pwEle.is_enabled())

#enter login details on the username and password section
userEle.send_keys("abc")
pwEle.send_keys("123")

#locate and store the login button on a variable
loginBtn=driver.find_element_by_name("login")
#click on the login button
loginBtn.click()


#go to the register page
driver.get("http://demo.automationtesting.in/Register.html")

#locate and store the male radio button on a variable
maleRadioBtn=driver.find_element_by_css_selector("input[value='Male']")

#click on the male radio button
maleRadioBtn.click()

#check if the male redio is selected, return turn of false
print("Is this radio button selected? ",maleRadioBtn.is_selected())

#locate and store the female radio button on a variable
femaleRadioBtn=driver.find_element_by_css_selector("input[value='FeMale']")

#check if the male redio is selected, return turn of false
print("Is this radio button selected? ",femaleRadioBtn.is_selected())