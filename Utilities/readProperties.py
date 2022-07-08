import configparser
from selenium import webdriver
from Utilities.time_stamp import Time

config = configparser.RawConfigParser()
config.read("..\Configuration\config.ini")

class ReadConfig:
    time_s = Time.time_Stamp()

    @staticmethod
    def getURL():
        url = config.get('common data','baseURL')
        return url

    @staticmethod
    def getLoginURL():
        url = config.get('common data', 'loginURL')
        return url

    @staticmethod
    def get_userEmail():
        email = config.get('common data',"userEmail")
        return email

    @staticmethod
    def get_userPWD():
        pwd = config.get('common data',"userPWD")
        return pwd

    @staticmethod
    def get_home_title():
        HomeTitle = config.get("page title","homePage")
        return HomeTitle

    @staticmethod
    def get_login_title():
        login = config.get("page title", "LogIn_page")
        return login

    @staticmethod
    def get_loggedIn_title():
        loggedIn = config.get("page title", "LoggedIn_page")
        return loggedIn

    @staticmethod
    def get_URL_new_USER():
        newUserURL = config.get("new account", "newUserURL")
        return newUserURL

    @staticmethod
    def get_new_email():
        email = config.get("new account", "email")
        return email

    @staticmethod
    def get_new_name():
        name = config.get("new account", "name")
        return name

    @staticmethod
    def get_new_lastname():
        lastname = config.get("new account", "lastname")
        return lastname

    @staticmethod
    def get_new_password():
        password = config.get("new account", "password")
        return password

    @staticmethod
    def get_other_info():
        other_info = config.get("new account", "other_info")
        return other_info

    @staticmethod
    def get_new_company():
        company = config.get("new account", "company")
        return company

    @staticmethod
    def get_new_date_of_birth():
        date_of_birth = config.get("new account", "date_of_birth")
        return date_of_birth

    @staticmethod
    def get_new_month_of_birth():
        month_of_birth = config.get("new account", "month_of_birth")
        return month_of_birth

    @staticmethod
    def get_new_year_of_birth():
        year_of_birth = config.get("new account", "year_of_birth")
        return year_of_birth

    @staticmethod
    def get_new_address():
        address = config.get("new account", "address")
        return address

    @staticmethod
    def get_new_city():
        city = config.get("new account", "city")
        return city

    @staticmethod
    def get_new_address2():
        address2 = config.get("new account", "address2")
        return address2

    @staticmethod
    def get_new_state():
        state = config.get("new account", "state")
        return state

    @staticmethod
    def get_new_zipcode():
        zipcode = config.get("new account", "zipcode")
        return zipcode

    @staticmethod
    def get_new_country():
        country= config.get("new account", "country")
        return country

    @staticmethod
    def get_new_home_phone():
        home_phone = config.get("new account", "home_phone")
        return home_phone

    @staticmethod
    def get_new_mobile_phone():
        mobile_phone = config.get("new account", "mobile_phone")
        return mobile_phone

    @staticmethod
    def get_new_alies_address():
        alies_address = config.get("new account", "alies_address")
        return alies_address


