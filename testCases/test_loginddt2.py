import pytest

from pageObjecct.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import XLUtils
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import time

class Test_002_DDT_Login:
    baseURL = ReadConfig.getApplicationURL()
    path= ".//testData/LoginData.xlsx"      #.// represents current project
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_login_DDT(self, setup):

        self.logger.info("******************Test_002_DDT_Login*********************")
        self.logger.info("***************Verifying Login Test is started***********************")
        self.driver = setup
        self.driver.get(self.baseURL)  # below lp is object of class LoginPage. Self because all variables belongs to class Test_001_Login
        self.lp = LoginPage(self.driver)  # hener e call login page, constructor is invokes which expects driver as paramereter whch we give(self.driver

        self.rows = XLUtils.getRowCount(self.path,'Sheet1')
        print("Number of rows in an excel",self.rows)


        list_status = []  #Empty list variable

        for r in range(2,self.rows+1):
            self.user = XLUtils.readData(self.path,'Sheet1',r,1)
            self.password = XLUtils.readData(self.path,'Sheet1',r,2)
            self.exp = XLUtils.readData(self.path, 'Sheet1',r, 3)

            self.lp.setUserName(self.user)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            time.sleep(10)





            act_title = self.driver.title
            if act_title == "Dashboard / nopCommerce administration":
                if self.exp =="Pass":
                    self.logger.info("***Passed***")
                    self.lp.clickLogout();

                    print("Logout clicked")
                    list_status.append("Pass")
                else:
                    self.logger.info("***Failed***")
                    self.lp.clickLogout();
                    list_status.append("Fail")



            elif act_title != "Dashboard / nopCommerce administration":
                if self.exp =="Pass":
                    self.logger.info("***Failed***")
                    list_status.append("Fail")
                elif self.exp == 'Fail':
                    self.logger.info("***Passed***")
                    list_status.append("Pass")


            if "Fail" not in list_status:
                self.logger.info("Login DDt test is passed...")

                assert True
            else:
                self.logger.info("Login DDt test is failed...")

                assert False


        self.logger.info("*****End of Login DDT Test****")
        self.logger.info("*****Test_002_DDT_Login*****")
        self.driver.close()





