from selenium.webdriver.common.by import By

class SearchPage:
    def __init__(self, driver):
        self.driver = driver

    search_box = (By.ID, "filter_keyword")
    search_button = (By.CLASS_NAME, "button-in-search")
    product_titles = (By.CSS_SELECTOR, ".prdocutname")

    def open(self):
        self.driver.get("https://automationteststore.com/")

    def search_product(self, keyword):
        self.driver.find_element(*self.search_box).clear()
        self.driver.find_element(*self.search_box).send_keys(keyword)
        self.driver.find_element(*self.search_button).click()

    def get_results(self):
        return self.driver.find_elements(*self.product_titles)