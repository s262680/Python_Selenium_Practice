from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome("C:\Webdrivers\chromedriver_win32\chromedriver")

driver.get("file:///C:/Users/K/Desktop/WebTable.html")

#returns all rows in the table
rows=driver.find_elements(By.XPATH, "/html/body/table/tbody/tr")

print("Number of rows: " + str(len(rows)))

#returns all columns in the table
cols=driver.find_elements(By.XPATH, "/html/body/table/tbody/tr[1]/th")
print("Number of cols: " + str(len(cols)))

#loop through the first row and return all header inside the table
for c in range(1, len(cols)+1):
    headers=driver.find_element(By.XPATH, "/html/body/table/tbody/tr[1]/th["+str(c)+"]").text
    # continous printing in the same line with some spaces between
    print(headers, end="  ")
# print nothing and jump to next line
print()

#loop through the table and return all values inside the table except the headers
for r in range(2, len(rows)+1):
    for c in range(1, len(cols)+1):
        value=driver.find_element(By.XPATH, "/html/body/table/tbody/tr["+str(r)+"]/td["+str(c)+"]").text
        #continous printing in the same line with some spaces between
        print(value, end="   ")
    #print nothing and jump to next line
    print()

