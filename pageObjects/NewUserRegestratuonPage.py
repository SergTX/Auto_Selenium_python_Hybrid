from selenium.webdriver.common.by import By
import time
import datetime

class New_User_Reg:

    email_new_user_box_by_id = "email_create"
    create_button_by_id = "SubmitCreate"
    alert_not_valid_email_by_id = "create_account_error"
    mr_title_by_id = 'id_gender1'
    first_name_by_id = "customer_firstname"
    last_name_by_id = 'customer_lastname'
    email_by_id = "email"
    password_by_id = "passwd"
    drop_down_days_by_id = "uniform-days"
    drop_down_month_by_id = "uniform-months"
    drop_down_year_by_id = "uniform-years"
    sec_first_name_by_id = "firstname"
    sec_last_name_by_id = "lastname"
    newsletter_check_box_by_id = "newsletter"
    company_name_by_id = "company"
    address_name_by_id = "address1"
    address_2_name_by_id = "address2"
    city_name_by_id = "city"
    drop_down_States_menu_by_id = "uniform-id_state"
    zip_code_by_id = "postcode"
    drop_down_Country_menu_by_id = "uniform-id_country"
    text_box_other_by_id = "other"
    home_phone_by_id = "phone"
    mobile_phone_by_id = "phone_mobile"
    my_address_alias_by_id = "alias"
    register_button_by_xpath = "//*[@id='submitAccount']/span"

    def __init__(self, driver):
        self.driver = driver

    def setNewEmail(self,newEmail):
        self.driver.find_element(By.ID, self.email_new_user_box_by_id).clear()
        self.driver.find_element(By.ID, self.email_new_user_box_by_id).send_keys(newEmail)

    def clickCreate(self):
        self.driver.find_element(By.ID, self.create_button_by_id).click()

    def setMrTitle(self):
        self.driver.find_element(By.ID, self.mr_title_by_id).click()

    def setFirstName(self,first_name):
        self.driver.find_element(By.ID, self.first_name_by_id).clear()
        self.driver.find_element(By.ID, self.first_name_by_id).send_keys(first_name)

    def setLastName(self, last_name):
        self.driver.find_element(By.ID, self.last_name_by_id).clear()
        self.driver.find_element(By.ID, self.last_name_by_id).send_keys(last_name)

    def setEmail(self, email):
        self.driver.find_element(By.ID, self.email_by_id).clear()
        self.driver.find_element(By.ID, self.email_by_id).send_keys(email)

    def check_New_email(self):
        check = self.driver.find_element(By.ID, self.email_by_id)
        return check.text


    def setPassWord(self, password):
        self.driver.find_element(By.ID, self.password_by_id).clear()
        self.driver.find_element(By.ID, self.password_by_id).send_keys(password)

    def setNewsLetter(self):
        self.driver.find_element(By.ID, self.newsletter_check_box_by_id).click()

    def setFirstName_2(self,first_name_2):
        self.driver.find_element(By.ID, self.sec_first_name_by_id).clear()
        self.driver.find_element(By.ID, self.sec_first_name_by_id).send_keys(first_name_2)

    def setLasttName_2(self,Last_name_2):
        self.driver.find_element(By.ID, self.sec_last_name_by_id).clear()
        self.driver.find_element(By.ID, self.sec_last_name_by_id).send_keys(Last_name_2)



    def setCompany(self, company):
        self.driver.find_element(By.ID,self.company_name_by_id).clear()
        self.driver.find_element(By.ID, self.company_name_by_id).send_keys(company)

    def setAddress(self, address):
        self.driver.find_element(By.ID, self.address_name_by_id).clear()
        self.driver.find_element(By.ID, self.address_name_by_id).send_keys(address)

    def setAddress2(self, address2):
        self.driver.find_element(By.ID, self.address_2_name_by_id).clear()
        self.driver.find_element(By.ID, self.address_2_name_by_id).send_keys(address2)


    def dropd_City(self):
        self.driver.find_element(By.ID, self.city_name_by_id).click()

    def dropd_State(self):
        self.driver.find_element(By.ID, self.drop_down_States_menu_by_id).click()

    def setZipCode(self, zipCode):
        self.driver.find_element(By.ID, self.zip_code_by_id).clear()
        self.driver.find_element(By.ID, self.zip_code_by_id).send_keys(zipCode)

    def dropd_Country(self):
        self.driver.find_element(By.ID, self.drop_down_Country_menu_by_id).click()


    def setOther_text(self, text_other):
        self.driver.find_element(By.ID, self.home_phone_by_id).clear()
        self.driver.find_element(By.ID, self.home_phone_by_id).send_keys(text_other)

    def setHomephone(self, homePhone):
        self.driver.find_element(By.ID, self.home_phone_by_id).clear()
        self.driver.find_element(By.ID, self.home_phone_by_id).send_keys(homePhone)

    def setMobilephone(self, mobilePhone):
        self.driver.find_element(By.ID, self.home_phone_by_id).clear()
        self.driver.find_element(By.ID, self.home_phone_by_id).send_keys(mobilePhone)

    def setAliasaddress(self, alias_address):
        self.driver.find_element(By.ID, self.my_address_alias_by_id).clear()
        self.driver.find_element(By.ID, self.my_address_alias_by_id).send_keys(alias_address)

    def clickRegister(self):
        self.driver.find_element(By.XPATH,self.register_button_by_xpath).click()