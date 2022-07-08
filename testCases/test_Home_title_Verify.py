import time
import pytest
import logging
from selenium import webdriver
from pageObjects.LoginPage import Loginpage
from Utilities.customLogger import LogGen
from Utilities.time_stamp import Time
from Utilities.readProperties import ReadConfig as rc


class Test_HomeTitle_001:
    #class variable - access by self.
    homeURL = rc.getURL()
    home_title = rc.get_home_title()

    logger = LogGen.logs()

    s_t = Time.time_Stamp() # time stamp added to screenshots for better trucking

    def test_homePageTitle(self,setup):
        self.driver = setup # self.because it belongs to the class
        self.driver.get(self.homeURL)
        self.logger.info("************************** Test_001  Launch Browser *************************")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.logger.info("************************** Receiving Home Title *************************")
        actual_title = self.driver.title
        time.sleep(3)
        self.logger.info("************************** Verifying Home Title *************************")
        if actual_title == self.home_title:
            assert True
            self.logger.info("************************** Title Matched *************************")
            print(f"\n Title matched")
            self.driver.save_screenshot('..\Screenshots\HomePageTitlePASSED.png' + self.s_t) # out of TCases and to Sc
            self.driver.close()
        else:
            self.logger.warning("************************** Title Not Matched *************************")
            print("\n Title not matching!")
            print(f'\n Actual title is :', actual_title, "\n Expected title is :", self.home_title)
            self.driver.save_screenshot('..\Screenshots\HomePageTitleFailed.png' + self.s_t)
            self.logger.info("************************** Test_001 Browser Closed *************************")
            self.driver.close()
            assert False
        self.logger.info("************************** Test_001 Browser Closed *************************")














# from pageObjects.HomePage import HomePage
# from pageObjects.LoginPage import Login
# from Utilities.readProperties import ReadConfig as RC
# # from Utilities.customLogger import LogGen
# import pytest
#
#
#
# # logger = LogGen.loggen()
# url = RC.getURL()
# titleHome = RC.get_home_title()
#
# class Home_Title:
#     def test_homeTitle(self,setup):
#         driver = setup
#         logger.info("**************************   Launch Browser  001 *************************")
#         driver.get(url)
#         logger.info("**************************   Open Home Page  001 *************************")
#         actual_title = driver.title
#         logger.info("********************** Verification of the title 001 *************************")
#         if actual_title == titleHome:
#             logger.info("********************** Verification Passed 001 *************************")
#             driver.save_screenshot(".\\Screenshots\\" + "HomePageTitlePassed.png")
#             assert True
#         else:
#             logger.info("********************** Verification Failed 001 *************************")
#             driver.save_screenshot(".\\Screenshots\\" + "HomePageTitleFailed.png")
#             assert False
#         logger.info("**************************   Closing Browser  001 *************************")
#         driver.close()
#
