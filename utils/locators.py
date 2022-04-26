from selenium.webdriver.common.by import By


# for maintainability we can seperate web objects by page name

class MainPageLocators(object):
    LOGO = (By.XPATH, '//div[@class=\'NavBar_logo__Rgo-5\']')
    # ACCOUNT = (By.ID, 'nav-link-accountList')
    SIGNUP = (By.XPATH, '//a[@href=\'/register?continue=https%3A%2F%2Ffullstack.edu.vn%2Fcourses%3F_type%3Dtab\']')
    LOGIN = (By.XPATH, '//a[@class=\'NavBar_loginBtn__5DxZL\']')
    SEARCH = (By.XPATH, '//input[@class=\'Search_input__GnMba\']')
    SEARCH_LIST = (By.XPATH, '//div[@class=\'ScrollList_body__iMN-l\']')
    COURSE_LINK = (By.XPATH, '//a[@class=\'Sidebar_active__uvck8\']')


class LoginPageLocators(object):
    EMAIL = (By.XPATH, '//input[@name=\'email\']')
    PASSWORD = (By.XPATH, '//input[@name=\'password\']')
    SUBMIT = (By.XPATH, '//button[@type=\'button\']')
    ERROR_MESSAGE = (By.XPATH, '//p[@class=\'Login_dontHaveAcc__l0kxL\']//text()')


class SearchPageLocators(object):
    SEARCH = (By.XPATH, '//input[@class=\'Search_input__GnMba\']')
    SEARCHCOURSE = (By.XPATH, '//div[@class=\'ScrollList_body__iMN-l\']')
