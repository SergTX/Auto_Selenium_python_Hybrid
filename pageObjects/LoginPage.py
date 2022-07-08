from selenium.webdriver.common.by import By


class Loginpage:
    email_box_by_id = "email"
    password_box_by_id = "passwd"
    click_SignIn_by_name = "SubmitLogin"
    click_sign_out_by_class = "logout"

    def __init__(self,driver):
        self.driver = driver   # self.because it belongs to the class

# actual methods

    def setUserName(self, username): # username will be provided at the actual testcase
        self.driver.find_element(By.ID, self.email_box_by_id).clear()
        self.driver.find_element(By.ID,self.email_box_by_id).send_keys(username)

    def setUserPwd(self,password): # pwd will be provided at atc
        self.driver.find_element(By.ID, self.password_box_by_id).clear()
        self.driver.find_element(By.ID, self.password_box_by_id).send_keys(password)

    def clickSignIn(self):
        self.driver.find_element(By.NAME, self.click_SignIn_by_name).click()

    def clickSignOut(self):
        self.driver.find_element(By.CLASS_NAME, self.click_sign_out_by_class).click()




# from selenium.webdriver.common.by import By
# from selenium import webdriver
# from Utilities.readProperties import ReadConfig as rc
#
# class Login:
#
#     email = rc.get_userEmail()
#     pwd = rc.get_userPWD()
#     email_box_by_id = "email"
#     password_box_by_id = "passwd"
#     click_SignIn_by_name = "SubmitLogin"
#
#     def __int__(self, driver):
#         self.driver = driver
#
#     def get_email(self):
#         email_box = self.driver.find_element(By.ID, self.email_box_by_id)
#         email_box.clear()
#         email_box.send_keys(self.email)
#
#     def get_password(self):
#         pwd_box = self.driver.find_element(By.ID, self.password_box_by_id)
#         pwd_box.clear()
#         pwd_box.send_keys(self.pwd)
#
#     def click_signIn(self):
#         self.driver.find_element(By.NAME, self.click_SignIn_by_name).click()
#
#
