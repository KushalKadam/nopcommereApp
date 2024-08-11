from pageObjecct.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_001_Login:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserEmail()
    password = ReadConfig.getUserPassword()

    logger = LogGen.loggen()

    # def test_homePageTitle(self, setup):
    #     self.driver = setup
    #     self.driver.get(self.baseURL)
    #     act_title = self.driver.title
    #     self.driver.close()
    #     if act_title == "Your store. Login1":
    #         assert True
    #         # self.driver.close()
    #     else:
    #         self.driver.save_screenshot(".\\screenshots\\"+"test_homePageTitle.png")
    #         assert False
    #         # self.driver.close()

    def test_homePageTitle(self, setup):
        try:
            # Initialize the driver
            self.logger.info("*******************Test_001_Login***************")
            self.logger.info("************Verifying Home Page Title************")#we use self to access logger which is in class
            self.driver = setup
            self.driver.get(self.baseURL)

            # Get the actual title of the page
            act_title = self.driver.title

            # Verify the title and handle the result
            if act_title == "Your store. Login":
                assert True
                self.logger.info("*****************Home Page Title Test is passed*****************************")
            else:
                # Save a screenshot if the title does not match
                self.logger.warn("***********************Home Page Title Test is failed*******************************")
                screenshot_path = ".\\screenshots\\test_homePageTitle.png"
                if self.driver.save_screenshot(screenshot_path):
                    print(f"Screenshot saved successfully at {screenshot_path}")
                else:
                    print(f"Failed to save screenshot at {screenshot_path}")
                assert False, f"Title mismatch: Expected 'Your store. Login1', but got '{act_title}'"
        except Exception as e:
            print(f"An error occurred: {e}")
            assert False, "Test failed due to an exception"
        finally:
            # Ensure the browser is closed even if an error occurs
            self.driver.close()

    def test_login(self, setup):
        try:
            self.logger.info("***************Verifying Login Test is started***********************")
            self.driver = setup
            self.driver.get(self.baseURL)  # below lp is object of class LoginPage. Self because all variables belongs to class Test_001_Login
            self.lp = LoginPage(self.driver)  # hener e call login page, constructor is invokes which expects driver as paramereter whch we give(self.driver
            self.lp.setUserName(self.username)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            act_title = self.driver.title
            if act_title == "Dashboard / nopCommerce administration":
                assert True
                self.logger.info("************Login Test is passed******************")
            else:
                screenshot1_path = ".\\screenshots\\" + "test_login.png"
                self.logger.error("***********************Home Page Title Test is failed*******************************")
                if self.driver.save_screenshot(screenshot1_path):
                    print(f"Screenshot saved successfully at {screenshot1_path}")
                else:
                    print(f"Failed to save screenshot at {screenshot1_path}")
                assert False, f"Title mismatch: Expected 'Dashboard / nopCommerce administration', but got '{act_title}'"
        except Exception as e:
            print(f"An error occurred: {e}")
            assert False, "Test failed due to an exception"

        finally:
            self.driver.close()

    # self.driver = setup
    #     self.driver.get(self.baseURL)    #below lp is object of class LoginPage. Self because all variables belongs to class Test_001_Login
    #     self.lp = LoginPage(self.driver)  #hener e call login page, constructor is invokes which expects driver as paramereter whch we give(self.driver
    #     self.lp.setUserName(self.username)
    #     self.lp.setPassword(self.password)
    #     self.lp.clickLogin()
    #     act_title= self.driver.title
    #     self.driver.close()
    #     if act_title == "Dashboard / nopCommerce administration":
    #         assert True
    #     else:
    #         self.driver.save_screenshot(".\\screenshots\\" + "test_login.png")
    #
    #         assert False
