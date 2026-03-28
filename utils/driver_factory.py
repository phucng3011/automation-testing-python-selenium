from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from utils.config_reader import ConfigReader

def get_driver():
    config = ConfigReader()

    browser = config.get_browser()

    if browser == "chrome":
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
    else:
        raise Exception("Browser not supported")

    driver.maximize_window()
    driver.implicitly_wait(config.get_timeout())

    return driver