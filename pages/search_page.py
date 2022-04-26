from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage
from pages.login_page import LoginPage
from pages.signup_page import SignUpBasePage
from utils.locators import *


class SearchPage(BasePage):

    def __init__(self, driver):
        self.locator = SearchPageLocators
        super(SearchPage, self).__init__(driver)  # Python2 version

    def enter_search_question(self, question):
        self.find_element(*self.locator.SEARCH).send_keys(question)
        self.find_element(*self.locator.SEARCH).send_keys(Keys.ENTER)

    def get_text_result(self):

         searchText = self.find_element(*self.locator.SEARCHCOURSE)
         return searchText

