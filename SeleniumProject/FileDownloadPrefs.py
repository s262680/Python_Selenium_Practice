from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

#Settings for Chrome

#create a variable for chrome preference options
chromeOptions=Options()
#setting preference options, first parameter is the key, second is the new location that we want to specify
chromeOptions.add_experimental_option("prefs",{"download.default_directory": "C:\TempForTesting"})
#apply preference options here
#driver = webdriver.Chrome(executable_path="C:\Webdrivers\chromedriver_win32\chromedriver", options=chromeOptions)


#Settings for Firefox

#create a variable for firefox preference options
firefoxPrefs=webdriver.FirefoxProfile()
#setting preference options, first parameter is the key with prevent the browser from showing the "Save To" pop-up
#second parameter is the file type that will have this preference applied
firefoxPrefs.set_preference("browser.helperApps.neverAsk.saveToDisk", "text/plain,application/pdf")
#prevent download box pop-up
firefoxPrefs.set_preference("browser.download.manager.showWhenStarting", False)
#set the specify download location
firefoxPrefs.set_preference("browser.download.dir", "C:\TempForTesting")
#The value of browser.download.folderList can be set to either 0, 1, or 2.
#When set to 0, Firefox will save all downloaded files to the user's desktop.
#When set to 1, these downloads will go to the Downloads folder.
#When set to 2, the location specified for the most recent download is used again.
firefoxPrefs.set_preference("browser.download.folderList", 2)
#disable pdf reader
firefoxPrefs.set_preference("pdfjs.disabled", True)
#apply preference options here
driver = webdriver.Firefox(executable_path="C:\Webdrivers\geckodriver-v0.29.1-win64\geckodriver", firefox_profile=firefoxPrefs)




driver.get("http://demo.automationtesting.in/FileDownload.html")

driver.maximize_window()

#download text file
driver.find_element(By.ID, "textbox").send_keys("Testing TXT")
driver.find_element(By.ID, "createTxt").click()
driver.find_element(By.ID, "link-to-download").click()

#download pdf file
driver.find_element(By.ID, "pdfbox").send_keys("Testing PDF")
driver.find_element(By.ID, "createPdf").click()
driver.find_element(By.ID, "pdf-link-to-download").click()
