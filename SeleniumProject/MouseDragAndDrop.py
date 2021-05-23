from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time
import re

driver = webdriver.Chrome("C:\Webdrivers\chromedriver_win32\chromedriver")

driver.get("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")

driver.maximize_window()


#locate dragable element and target element
dragEle=driver.find_element(By.ID, "box6")
targetEle=driver.find_element(By.ID, "box106")

#create class obj to perform mouse actions
actions=ActionChains(driver)

#perform drag and drop action
#actions.drag_and_drop(dragEle,targetEle).perform()

#create list objects for dragables and targetables
dragEles=[]
targetEles=[]

#store all dragables and targetables in list objects
for x in range(1, 8):
    dragEles.append(driver.find_element(By.ID, "box"+str(x)))
    targetEles.append(driver.find_element(By.ID, "box10"+str(x)))

#perform drag and drop action for all the drapables and targetables
for d, t in zip(dragEles, targetEles):
    actions.drag_and_drop(d, t).perform()


    #d = str(d).replace("[", "").replace("]", "")
    #t = str(t).replace("[", "").replace("]", "")