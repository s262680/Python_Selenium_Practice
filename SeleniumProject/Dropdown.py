from selenium import webdriver

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import Select

import time

driver = webdriver.Chrome("C:\Webdrivers\chromedriver_win32\chromedriver")

driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")

element=driver.find_element(By.ID, "RESULT_RadioButton-9")

#get the dropdown list items by using the Select fucntion, then store it into a variable
dropdown=Select(element)

print(len(dropdown.options))

#store all options into a variable
allOptions=dropdown.options

#print each option in the list
for option in allOptions:
    print(option.text)

#Select by visible text
#dropdown.select_by_visible_text("Morning")

#Select by index
#dropdown.select_by_index(2) #select afternoon

#Select by value
#dropdown.select_by_value("Radio-2") #select evening

#select each of the item in the list
for x in range(0, len(dropdown.options)):
    dropdown.select_by_index(x)
    time.sleep(1)