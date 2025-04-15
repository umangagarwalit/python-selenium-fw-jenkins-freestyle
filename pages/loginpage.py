from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from pages.homepage import HomePage

class LoginPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

        self.username = (By.XPATH, "//*[@name='username']")
        self.password = (By.XPATH, "//*[@name='password']")
        self.login_button = (By.XPATH, "//*[@value='Log In']")

    def enter_username(self, uname):
        self.driver.find_element(*self.username).send_keys(uname)

    def enter_password(self, upass):
        self.driver.find_element(*self.password).send_keys(upass)

    '''
    def click_login(self):
        self.driver.find_element(*self.login_button).click()
    '''

    #OR

    def click_login(self):
        self.driver.find_element(*self.login_button).click()
        return HomePage

    # OR
    def do_login(self, uname, upass):
        self.enter_username(uname)
        self.enter_password(upass)
        self.click_login()
        return HomePage
