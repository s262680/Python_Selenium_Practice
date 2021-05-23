from selenium import webdriver
from selenium.webdriver.common.by import By
import ExcelFunctions
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver=webdriver.Chrome(executable_path="C:\Webdrivers\chromedriver_win32\chromedriver")

driver.maximize_window()

driver.get("https://opensource-demo.orangehrmlive.com/index.php/dashboard")

xlPath="C:\TempForTesting\Book.xlsx"

#get the number of rows and columns
rows= ExcelFunctions.getRowCount(xlPath, "LoginDetails")
columns= ExcelFunctions.getRowCount(xlPath, "LoginDetails")


for r in range(2, rows+1):
    #read the username and password in each rows
    username = ExcelFunctions.readData(xlPath, "LoginDetails", r, 1)
    password = ExcelFunctions.readData(xlPath, "LoginDetails", r, 2)

    #locate the username box, password box and login button on the website
    driver.find_element(By.ID, "txtUsername").send_keys(username)
    driver.find_element(By.ID, "txtPassword").send_keys(password)
    driver.find_element(By.ID, "btnLogin").click()

    #wait briefly after click the login button
    time.sleep(1)

    #check if the "welcome" element is exist, this element only available after successful login
    #if the element is available then present will be set to True, otherwise it will set to False
    presence= None
    try:
        driver.find_element(By.ID, "welcome")
        presence=True
    except NoSuchElementException:
        presence=False

    #if present is True then that mean we are on the next page and the login is successful
    if presence==True:
        print(str(r-1)+" Test is passed")
        #enter "Pass" as result in the third column of the "LoginDetails" excel sheet
        ExcelFunctions.writeData(xlPath, "LoginDetails", r, 3, "Pass")
        #click on the User drop down list, wait until the "logout" button is visiable then click on it to go back to the login page
        driver.find_element(By.ID, "welcome").click()
        wait = WebDriverWait(driver, 10)
        ele = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Logout")))
        ele.click()
    #present is False, enter "Fail as result in the third column of the "LoginDetails" excel sheet
    else:
        print(str(r-1)+" Test is failed")
        ExcelFunctions.writeData(xlPath, "LoginDetails", r, 3, "Fail")

