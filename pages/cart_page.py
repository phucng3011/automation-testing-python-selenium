from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

class CartPage:
    def __init__(self, driver):
        self.driver = driver

    first_product = (By.CSS_SELECTOR, ".fixed_wrapper")
    add_to_cart_btn = (By.CSS_SELECTOR, ".productcart")
    cart_button = (By.ID, "main_menu_top")
    cart_link = (By.XPATH, "//a[contains(@href,'checkout/cart')]")
    cart_items = (By.CSS_SELECTOR, ".table tbody tr")

    def open(self):
        self.driver.get("https://automationteststore.com/")

    def add_first_product_to_cart(self):
        buttons = self.driver.find_elements(*self.add_to_cart_btn)
        buttons[0].click()

    def open_cart(self):
        self.driver.get("https://automationteststore.com/index.php?rt=checkout/cart")

    def get_cart_items(self):
        return self.driver.find_elements(*self.cart_items)