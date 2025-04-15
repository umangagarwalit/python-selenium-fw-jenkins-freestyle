
import pytest
import time

from utility.utility import launch_browser, launch_app, close_browser

@pytest.fixture(scope="function")
def setup_teardown():
    driver = launch_browser()
    time.sleep(1)

    launch_app(driver)
    time.sleep(1)

    yield driver

    time.sleep(1)
    close_browser(driver)