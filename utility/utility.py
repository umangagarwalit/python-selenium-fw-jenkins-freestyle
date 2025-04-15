from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from config import config

def launch_browser():
    service = Service(config.chrome_driver_path)
    driver = webdriver.Chrome(service=service)
    return driver

def launch_app(driver):
    driver.get(config.url)

def close_browser(driver):
    driver.quit()

def get_page_title(driver):
    return driver.title

