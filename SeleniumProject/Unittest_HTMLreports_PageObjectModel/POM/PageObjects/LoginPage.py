from selenium.webdriver.common.keys import Keys

class LoginPage():
    #locator of all the elements
    textbox_user_id = "Email"
    textbox_pw_id = "Password"
    button_login_xpath = "/html/body/div[6]/div/div/div/div/div[2]/div[1]/div/form/div[3]/button"
    button_logout_linktext = "Logout"

    #constructor which will excute everytime the class is called
    def __init__(self, driver):
        self.driver=driver

    def clearUserName(self, username):
        self.driver.find_element_by_id(self.textbox_user_id).send_keys(Keys.CONTROL + "a")
        self.driver.find_element_by_id(self.textbox_user_id).send_keys(Keys.DELETE)

    def clearPassword(self, password):
        self.driver.find_element_by_id(self.textbox_pw_id).send_keys(Keys.CONTROL + "a")
        self.driver.find_element_by_id(self.textbox_pw_id).send_keys(Keys.DELETE)

    def setUserName(self, username):
        self.driver.find_element_by_id(self.textbox_user_id).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element_by_id(self.textbox_pw_id).send_keys(password)

    def clickLogin(self):
        self.driver.find_element_by_xpath(self.button_login_xpath).click()

    def clickLogout(self):
        self.driver.driver.find_element_by_link_text(self.button_logout_linktext).click()
