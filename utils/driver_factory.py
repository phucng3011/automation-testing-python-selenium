from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from utils.config_reader import ConfigReader

def get_driver():
    config = ConfigReader()
    browser = config.get_browser()

    if browser == "chrome":
        chrome_options = Options()

        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")

        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=chrome_options)
    else:
        raise Exception("Browser not supported")

    driver.maximize_window()
    driver.implicitly_wait(config.get_timeout())

    return driver