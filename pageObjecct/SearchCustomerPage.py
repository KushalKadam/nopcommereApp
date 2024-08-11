from selenium.webdriver.common.by import By
class SearchCustomer():
    #Add Customer page
    txtEmail_id = "SearchEmail"
    txtFirstName_id = "SearchFirstName"
    txtLastName_id = "SearchLastName"
    btnSearch_id = "search-customers"
    tblSearchResults_xpath = "//table[@role='grid']"
    table_xpath = "//table[@id='customers-grid']"
    tableRows_xpath = "//table[@id='customers-grid']//tbody/tr"
    tableColumns_xpath = "//table[@id='customers-grid']//tbody/tr/td"

    def __init__(self, driver):
        self.driver = driver

    def setEmail(self, email):
        self.driver.find_element(By.ID,"SearchEmail").clear()
        self.driver.find_element(By.ID,"SearchEmail").send_keys(email)

    def setFirstName(self, fname):
        self.driver.find_element(By.ID,"SearchFirstName").clear()
        self.driver.find_element(By.ID, "SearchFirstName").send_keys(fname)

    def setLastName(self, lname):
        self.driver.find_element(By.ID, "SearchLastName").clear()
        self.driver.find_element(By.ID,"SearchLastName").send_keys(lname)

    def clickSearch(self):
        self.driver.find_element(By.ID, "search-customers").click()

    def getNoOfRows(self):
        return len(self.driver.find_element(By.XPATH, "//table[@id='customers-grid']//tbody/tr"))

    def getNoOfColumns(self):
        return len(self.driver.find_element(By.XPATH, "//table[@id='customers-grid']//tbody/tr/td"))

    def searchCustomerByEmail(self, email):
        flag = False
        for r in range(1, self.getNoOfRows()+1):
            table = self.driver.find_element(By.XPATH, "//table[@id='customers-grid']")
            emailid = table.find_element(By.XPATH, "//table[@id='customers-grid']//tbody/tr['+str(r)+']/td[2]").text
            if emailid == email:
                flag = True
                break
        return flag

    def searchCustomerByName(self, Name):
        flag = False
        for r in range(1, self.getNoOfRows()+1):
            table = self.driver.find_element(By.XPATH, "//table[@id='customers-grid']")
            name = table.find_element(By.XPATH, "//table[@id='customers-grid']//tbody/tr['+str(r)+']/td[3]").text
            if name == Name:
                flag = True
                break
        return flag
