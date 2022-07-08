import time
import pytest
from selenium import webdriver
from Utilities.customLogger import LogGen
from pageObjects.LoginPage import Loginpage
from Utilities.time_stamp import Time
from Utilities.readProperties import ReadConfig as rc


class Test_002_Login:

    logURL = rc.getLoginURL()
    username = rc.get_userEmail()
    password = rc.get_userPWD()
    title_SignedIn = rc.get_loggedIn_title()
    s_t = Time.time_Stamp()  # time stamp added to screenshots for better trucking
    logger = LogGen.logs()

    def test_login(self, setup):
        self.driver = setup
        self.logger.info("************************** Test_002  Launch Browser *************************")
        self.logger.info("************************** Open Login Page *************************")
        self.driver.get(self.logURL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        # to access loginpage.py and use all methods - need to create an object of the class
        self.lp = Loginpage(self.driver) # add self to lp because its inside testlogin class
        # beacause loginpage class has a construtor with driver then we pass driver with self (inside other class)
        self.logger.info("**************************  Enter User Email *************************")
        self.lp.setUserName(self.username)
        self.logger.info("**************************  Enter User Password *************************")
        self.lp.setUserPwd(self.password)
        self.driver.save_screenshot('..\Screenshots\Email_and_Pwd.png' + self.s_t)
        self.logger.info("**************************  Click Sign In *************************")
        self.lp.clickSignIn()
        self.logger.info("************************** Receiving Loged In Page Title *************************")
        actual_title = self.driver.title
        self.logger.info("************************** Verifying Title *************************")
        if actual_title == self.title_SignedIn:
            print(f"\n Title matched")
            self.logger.info("************************** Title Matched *************************")
            self.driver.save_screenshot('..\Screenshots\LoginPageTitlePASSED.png' + self.s_t)
            assert True
        else:
            print("\n Title not matching!")
            print(f'\n Actual title is :', actual_title, "\n Expected title is :", self.title_SignedIn)
            self.logger.warning("************************** Title Not Matched *************************")
            self.logger.info("************************** Test_002 Browser Closed *************************")
            self.driver.save_screenshot('..\Screenshots\LoginTitleFAILED.png' + self.s_t)
            self.driver.close()
            assert False


        time.sleep(3)
        self.logger.info("************************** Sign Out from Account *************************")
        self.lp.clickSignOut()
        self.driver.close()
        self.logger.info("************************** Test_002 Browser Closed *************************")


