import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, WebDriverException
from pageObject.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import XLUtils


class Test_002_DDT_Login:
    baseURL = ReadConfig.getApplicationURL()
    path = ".//testData/LoginData.xlsx"
    logger = LogGen.loggen()

    def test_login_DDT(self, setup):
        self.logger.info("******************Test_002_DDT_Login*********************")
        self.logger.info("***************Verifying Login Test is started***********************")

        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)

        self.rows = XLUtils.getRowCount(self.path, 'Sheet1')
        print("Number of rows in Excel:", self.rows)

        list_status = []

        for r in range(2, self.rows + 1):
            self.user = XLUtils.readData(self.path, 'Sheet1', r, 1)
            self.password = XLUtils.readData(self.path, 'Sheet1', r, 2)
            self.exp = XLUtils.readData(self.path, 'Sheet1', r, 3)

            self.lp.setUserName(self.user)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()

            try:
                WebDriverWait(self.driver, 10).until(EC.title_contains("Dashboard / nopCommerce administration"))
                act_title = self.driver.title
                if self.exp == "Pass":
                    self.logger.info("***Passed***")
                    self.lp.clickLogout()
                    list_status.append("Pass")
                else:
                    self.logger.info("***Failed***")
                    self.lp.clickLogout()
                    list_status.append("Fail")
            except TimeoutException:
                act_title = self.driver.title
                if self.exp == "Pass":
                    self.logger.info("***Failed***")
                    list_status.append("Fail")
                else:
                    self.logger.info("***Passed***")
                    list_status.append("Pass")
            except WebDriverException as e:
                self.logger.error(f"WebDriver Exception occurred: {str(e)}")
                list_status.append("Error")

        if "Fail" not in list_status:
            self.logger.info("Login DDT test is passed...")
            assert True
        else:
            self.logger.info("Login DDT test is failed...")
            assert False

        self.driver.close()
        self.logger.info("*****End of Login DDT Test****")
        self.logger.info("*****Test_002_DDT_Login*****")