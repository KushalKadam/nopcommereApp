from selenium import webdriver
from selenium.webdriver.common import by
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    # textbox_username_xpath = "//*[@id='Email']"
    # textbox_password_id = "Password"
    # button_login_xpath = "//*[@id='main']/div/div/div/div[2]/div[1]/div/form/div[3]/button"
    # link_logout_linktext = "Logout"

    def __init__(self, driver):  #Constructor: will automatially invoke at the time f object creation
        self.driver = driver  #self.driver is a class driver
        self.wait = WebDriverWait(self.driver, 10)

    def setUserName(self,username):
        email  = self.wait.until(EC.presence_of_element_located((By.ID, "Email")))
        self.driver.find_element(By.ID, "Email").clear()

        self.driver.find_element(By.ID, "Email").send_keys(username)

    def setPassword(self,password):
        self.driver.find_element(By.ID, "Password").clear()
        self.driver.find_element(By.ID, "Password").send_keys(password)

    def clickLogin(self):
        submit = self.wait.until(EC.presence_of_element_located((By.XPATH, "//*[@type='submit']")))
        submit.click()

    def clickLogout(self):
        self.driver.find_element(By.LINK_TEXT, "Logout").click()