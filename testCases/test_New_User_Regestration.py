from datetime import time

from selenium import webdriver
from Utilities.readProperties import ReadConfig as rc
from Utilities.time_stamp import Time
from Utilities.customLogger import LogGen
from pageObjects.NewUserRegestratuonPage import New_User_Reg


class Test_003_New_USER:

    time_s = Time.time_Stamp()

    email = f"NewUser{time_s}@mail.com"

    logUrl = rc.get_URL_new_USER()
    name = rc.get_new_name()
    lastname = rc.get_new_lastname()
    password = rc.get_new_password()
    company = rc.get_new_company()
    info = rc.get_other_info()
    dateB = rc.get_new_date_of_birth()
    monthB = rc.get_new_month_of_birth()
    yearB = rc.get_new_year_of_birth()
    homePhone = rc.get_new_home_phone()
    mobilePhone = rc.get_new_mobile_phone()
    zipcode = rc.get_new_zipcode()
    state = rc.get_new_state()
    country = rc.get_new_country()
    alies_address = rc.get_new_alies_address()
    city = rc.get_new_city()
    address = rc.get_new_address()
    address2 = rc.get_new_address2()


    s_t = Time.time_Stamp()
    logger = LogGen.logs()

    def test_create_new_user(self, setup):
        self.driver = setup

        self.driver.get(self.logUrl)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

        self.nu = New_User_Reg(self.driver)

        actual_email = self.nu.setNewEmail(self.email)


        self.nu.clickCreate()

        self.nu.setMrTitle()

        self.nu.setFirstName(self.name)

        self.nu.setLastName(self.lastname)

        current_email = self.nu.check_New_email()

        try:
            if current_email == actual_email:
                pass
                print("Matched")
                assert True

        except:
            self.nu.setEmail(self.email)
            assert False


        self.nu.setPassWord(self.password)



        # if self.nu.check_New_email() == self.nu.setNewEmail(self.email):
        #     print(f"text of {self.nu.check_New_email()}")
        #     pass
        # else:
        #     self.nu.setEmail(self.email)











