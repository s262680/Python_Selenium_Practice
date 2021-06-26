import time
import mysql.connector

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(executable_path="C:\Webdrivers\chromedriver_win32\chromedriver")
driver.get("https://opensource-demo.orangehrmlive.com/index.php/dashboard")
driver.maximize_window()


db=mysql.connector.connect(host="localhost", user="root", password="123456")

cur=db.cursor()

query1="insert into sakila.actor values ('203','test','guy','2006-02-15 04:34:33')"
query2="update sakila.actor set first_name='Python_tester' where actor_id='203'"
query3="delete from sakila.actor where actor_id='203'"
query4="SELECT * FROM sakila.actor"
query5="SELECT * FROM logintest.user"

cur.execute(query5)

#print all the columns in the console
#for cols in cur:
    #print(cols[0],"   ",cols[1],"   ",cols[2],"   ",cols[3])


for cols in cur:
    driver.find_element_by_id("txtUsername").send_keys(cols[1])
    driver.find_element_by_id("txtPassword").send_keys(cols[2])
    driver.find_element_by_id("btnLogin").click()
    time.sleep(3)


    presence= None
    try:
        driver.find_element(By.ID, "welcome")
        presence=True
    except NoSuchElementException:
        presence=False

    if presence==True:
        print("Test is passed")
        driver.find_element(By.ID, "welcome").click()
        wait = WebDriverWait(driver, 10)
        ele = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Logout")))
        ele.click()
    else:
        print("Test is failed")



cur.close()
#must commit before close otherwise the change will not be saved
db.commit()
db.close()

print("Completed")