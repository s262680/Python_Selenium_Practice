from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome("C:\Webdrivers\chromedriver_win32\chromedriver")

driver.get("https://opensource-demo.orangehrmlive.com/")

#enter login detail and click on the login button
driver.find_element(By.ID, "txtUsername").send_keys("Admin")
driver.find_element(By.ID, "txtPassword").send_keys("admin123")
driver.find_element(By.ID, "btnLogin").click()

#locate the menu elements on the next page
admin=driver.find_element(By.XPATH, "//*[@id='menu_admin_viewAdminModule']/b")
userMang=driver.find_element(By.ID, "menu_admin_UserManagement")
user=driver.find_element(By.ID, "menu_admin_viewSystemUsers")

#create action class obj, which provide methods that handle multiple mouse actions
action=ActionChains(driver)

#perform a series of mouse hovering actions and click on the user tab at the end
action.move_to_element(admin).move_to_element(userMang).move_to_element(user).click().perform()