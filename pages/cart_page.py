from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class CartPage(BasePage):

    add_to_cart_btn = (By.CSS_SELECTOR, ".productcart")
    cart_items = (By.CSS_SELECTOR, ".table tbody tr")

    def open(self):
        self.open_url()

    def open_cart(self):
        route = self.config.get_route("cart")
        self.open_url(route)

    def add_first_product_to_cart(self):
        wait = WebDriverWait(self.driver, 10)
        buttons = wait.until(
            EC.presence_of_all_elements_located(self.add_to_cart_btn)
        )
        buttons[0].click()

    def get_cart_items(self):
        return self.driver.find_elements(*self.cart_items)