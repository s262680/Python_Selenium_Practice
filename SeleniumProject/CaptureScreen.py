from selenium import webdriver

driver=webdriver.Chrome(executable_path="C:\Webdrivers\chromedriver_win32\chromedriver")

driver.maximize_window()

driver.get("https://opensource-demo.orangehrmlive.com/index.php/dashboard")

#take screenshot of the current page
driver.save_screenshot("C:\TempForTesting\screenshot\HomePage.png")

#take screenshot of the current page, return false if there is an IO error, else reture true
print(driver.get_screenshot_as_file("C:\TempForTesting\screenshot\HomePage2.png"))