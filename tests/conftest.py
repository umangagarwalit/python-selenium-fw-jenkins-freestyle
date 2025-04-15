
# Keep conftest.py under tests folder, if you want to run tests from PyCharm play button
# Keep conftest.py under project folder, if you want to run tests from PyCharm terminal
# If you want to run tests from PyChram play button as well as terminal, create pytest.ini file at project level having some info

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