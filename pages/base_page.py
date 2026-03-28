from utils.config_reader import ConfigReader

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.config = ConfigReader()

    def open_url(self, route=""):
        base_url = self.config.get_base_url()
        full_url = base_url + route
        self.driver.get(full_url)