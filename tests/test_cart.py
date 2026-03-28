import pytest
from utils.driver_factory import get_driver
from pages.cart_page import CartPage

@pytest.fixture
def driver():
    driver = get_driver()
    yield driver
    driver.quit()

def test_add_product_to_cart(driver):
    cart = CartPage(driver)
    cart.open()
    cart.add_first_product_to_cart()
    cart.open_cart()

    items = cart.get_cart_items()
    assert len(items) > 0


def test_cart_empty_initially(driver):
    cart = CartPage(driver)
    cart.open_cart()

    items = cart.get_cart_items()
    assert len(items) == 0