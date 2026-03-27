import pytest
from utils.driver_factory import get_driver
from pages.search_page import SearchPage

@pytest.fixture
def driver():
    driver = get_driver()
    yield driver
    driver.quit()

def test_search_valid_product(driver):
    search = SearchPage(driver)
    search.open()
    search.search_product("shampoo")

    results = search.get_results()
    assert len(results) > 0


def test_search_invalid_product(driver):
    search = SearchPage(driver)
    search.open()
    search.search_product("abcdefxyz123")

    results = search.get_results()
    assert len(results) == 0