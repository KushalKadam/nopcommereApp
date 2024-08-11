import pytest
import time
from pageObjecct.LoginPage import LoginPage
from pageObjecct.AddPayeePage import AddCustomer
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig
import string
import random


def random_generator():
    pass


class Test_003_AddCustomer:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserEmail()
    password = ReadConfig.getUserPassword()
    logger = LogGen.loggen()

    @pytest.mark.sanity
    def test_addCustomer(self, setup):
        self.logger.info("*******Test_003_AddCustomer*******")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("*****Login successful******")

        self.logger.info("******Starting Add Customer Test*******")
        self.addcust = AddCustomer(self.driver)
        self.addcust.clickOnCustomerMenu()
        self.addcust.clickOnCustomerMenuItem()
        self.addcust.clickOnAddNew()

        self.logger.info("*****Providing customer Info*****")
        self.email = random_generator() + "@gmail.com"
        self.addcust.setEmail(self.email)
        self.addcust.setPassword("test123")
        self.addcust.setCustomerRoles("Guests")
        self.addcust.setManagerofVendor("vendor 2")
        self.addcust.setGender("Male")
        self.addcust.setFirstName("Kushal")
        self.addcust.setLastName("Kadam")
        self.addcust.setDob("11/09/1995")
        self.addcust.setCompanyName("busyQA")
        self.addcust.setAdminContent("This is for testing....")
        self.addcust.clickOnSave()

        self.logger.info("*****Saving customer info*****")

        self.logger.info("****Add customer validation started***")

        self.msg = self.driver.find_element_by_tag_name("body").text

        print(self.msg)
        if 'customer has been added successfully.' in self.msg:
            assert True == True
            self.logger.info("****Add customer test passed****")
        else:
            self.driver.save_screenshot(".\\Screnshots\\" + "test_addCustomer_src.png")  #Screenshot
            self.logger.error("***Add customer test failed**")
            assert True == False

        self.driver.close()
        self.logger.info("***Ending Add Customer Test***")


def random_generator(size = 8, chars = string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))







