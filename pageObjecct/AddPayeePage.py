import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By


class AddCustomer:
    # Add customer page
    lnkCustomer_menu_xpath = "//a[@href='#']//span[contains(text(),'Customers')]"
    lnkCustomer_menuitem_xpath = "//span[@class'menu-item-title'][contains(text(),'Customers')]"
    btnAddnew_xpath = "//a[@class='btn btn-primary']"
    txtEmail_xpth = "//*[@id='Email']"
    txt_Password_xpath = "//*[@id='Password']"
    txtCustomerRoles_xpath = "//div[@class='k-multiselect-wrap k-floatwarp']"
    lstitemsAdministrators_xpath = "//li[contains(text(),'Adminitrators')]"
    lstitemsRegistered_xpath = "//li[contains(text(),'Registered')]"
    lstitemsGuests_xpath = "//li[contains(text(),'Registered')]"
    lstitemsVendors_xpath = "//li[contains(text(),'Vendors')]"
    drpmgrOfVendor_xpath = "//*[@id='VendorID']"
    rdMaleGender_id = "Gender_Male"
    rdFemaleGender_id = "Gender_Female"
    txtFirstName_xpath = "//*[@id='FirstName']"
    txtLastName_xpath = "//*[@id='LastName']"
    txtDob_xpath = "//*[@id='DateOfBirth']"
    txtCompanyName_xpath = "//*[@id='Company']"
    txtAdminConmment_xpath = "//*[@id='AdminComment']"
    btnSave_xpath = "/html/body/div[3]/div[1]/form/div[1]/div/button[1]"

    def __init__(self,driver):
        self.driver = driver

    def clickOnCustomerMenu(self):
        self.driver.find_element(By.XPATH,"//a[@href='#']").click()

    def clickOnCustomerMenuItem(self):
        self.driver.find_element(By.XPATH,"/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[4]/ul/li[1]/a/p").click()

    def clickOnAddNew(self):
        self.driver.find_element_by_xpath(self.btnAddnew_xpath).click()

    def clickOnSave(self):
        self.driver.find_element_by_Xpath(self.btnSave_xpath).click()

    def setEmail(self,email):
        self.driver.find_element_by_Xpath(self.txtEmail_xpth).send_keys(email)

    def setPassword(self,password):
        self.driver.find_element_by_Xpath(self.txt_Password_xpath).send_keys(password)

    def setCustomerRoles(self,role):
        self.driver.find_element_by_Xpath(self.txtCustomerRoles_xpath).click()
        time.sleep(3)
        if role == 'Registered':
            self.listitem = self.driver.find_element_by_Xpath(self.lstitemsRegistered_xpath)
        elif role == 'Administrators':
            self.listitem = self.driver.find_element_by_Xpath(self.lstitemsAdministrators_xpath)
        elif role == 'Guest':
            #Here user can be Registered (or) Guest, only one
            time.sleep(3)
            self.driver.find_element_by_xpath("//*[@id='SelectedCustomerzRoleIds_taglist']/li/span[2]").click()
            self.listitem = self.driver.find_element_by_Xpath(self.lstitemsGuests_xpath)
        elif role == 'Registered':
            self.listitem = self.driver.find_element_by_Xpath(self.lstitemsRegistered_xpath)
        elif role == 'Vendor':
            self.listitem = self.driver.find_element_by_Xpath(self.lstitemsVendors_xpath)
        else:
            self.listitem = self.driver.find_element_by_Xpath()

    def setManagerofVendor(self, value):
        drp = Select(self.driver.find_element_by_xpath(self.lstitemsVendors_xpath))
        drp.select_by_visible_text(value)

    def setGender(self, gender):
        if gender == 'Male':
            self.driver.find_element_by_id(self.rdMaleGender_id)
        elif gender == 'Female':
            self.driver.find_element_by_id(self.rdFemaleGender_id)
        else:
            self.driver.find_element_by_id(self.rdMaleGender_id)


    def setFirstName(self, fname):
        self.driver.find_element_by_xpath(self.txtFirstName_xpath)

    def setLastName(self, lname):
        self.driver.find_element_by_xpath(self.txtLastName_xpath)

    def setDob(self, dob):
        self.driver.find_element_by_xpath(self.txtDob_xpath)

    def setCompanyName(self, setcompanyname):
        self.driver.find_element_by_xpath(self.txtCompanyName_xpath)

    def setAdminContent(self, setadmincontent):
        self.driver.find_element_by_xpath(self.txtAdminConmment_xpath)









