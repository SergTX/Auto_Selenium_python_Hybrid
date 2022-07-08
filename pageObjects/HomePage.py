# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
#
# class HomePage:
#     # locators from Home page
#     link_to_signIn_by_name = "login"
#     search_box_by_id = "search_query_top"
#     shopping_cart_by_text = "View my shopping cart"
#     link_woman_by_text = "Women"
#     link_dresses_by_text = "Dresses"
#     link_T_shirts_by_text = "T-shirts"
#     link_popular_by_xpath = "//*[@id='home-page-tabs']/li[1]/a"
#     link_BestSellers_by_xpath = "//*[@id='home-page-tabs']/li[2]/a"
#     search = "dress"
#
#     def __int__(self,driver):
#         self.driver = driver
#
#     def clickOnLogin(self):
#         click = self.driver.find_element(By.CLASS_NAME, self.link_to_signIn_by_name)
#         click.click()
#
#     def clickOnSearchBox(self):
#         search_box = self.driver.find_element(By.ID,self.search_box_by_id)
#         search_box.clear()
#         search_box.send_keys(self.search)
#
#     def clickShopCart(self):
#         self.driver.find_element(By.LINK_TEXT, self.shopping_cart_by_text).click()
#
#     def clickWoman_link(self):
#         self.driver.find_element(By.LINK_TEXT,self.link_woman_by_text).click()
#
#     def clickDresses_link(self):
#         self.driver.find_element(By.LINK_TEXT, self.link_dresses_by_text).click()
#
#     def clickTshirts_link(self):
#         self.driver.find_element(By.LINK_TEXT, self.link_T_shirts_by_text).click()
#
#     def clickPopular_link(self):
#         self.driver.find_element(By.XPATH, self.link_popular_by_xpath).click()
#
#     def clickPopular(self):
#         self.driver.find_element(By.XPATH,self.link_BestSellers_by_xpath).click()
