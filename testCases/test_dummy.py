import time
import datetime
from Utilities.time_stamp import Time


# time_stamp = time.time()
# s_t = datetime.datetime.fromtimestamp(time_stamp).strftime('   %Y_%b_%d_%H_%M_%p')


from selenium import webdriver
class Test_tesr:
    def test_test(self):
        self.driver = webdriver.Edge()

        self.s_t = Time.time_Stamp()
        self.driver.get("https://stackoverflow.com/questions/55110504/browser-save-screenshot-is-not-working-as-expected")
        self.driver.maximize_window()
        self.driver.save_screenshot("C:\serge\OneDrive\Desktop\HybridFramework\Screenshots\dummy.png")
        time.sleep(4)
        self.driver.save_screenshot('..\Screenshots\dumm.png' + self.s_t)
        self.driver.close()
