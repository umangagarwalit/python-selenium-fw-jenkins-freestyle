import time
from pages.loginpage import LoginPage
from config import config
from utility import utility


def test_01(setup_teardown):
    driver = setup_teardown
    login_page = LoginPage(driver)

    #Way1
    home_page = login_page.do_login(config.username_value, config.password_value)

    '''
    #Way2
    login_page.enter_username(config.username_value)
    login_page.enter_password(config.password_value)
    home_page = login_page.click_login()
    '''

    time.sleep(2)

    assert utility.get_page_title(driver) == "ParaBank | Accounts Overview", "Page title does not match"

    print(utility.get_page_title(driver))
