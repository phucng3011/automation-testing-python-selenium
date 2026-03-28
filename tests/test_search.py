import pytest
from utils.driver_factory import get_driver
from pages.search_page import SearchPage
from utils.data_reader import load_test_data

test_data = load_test_data("data/testdata.json")["search"]

@pytest.fixture
def driver():
    driver = get_driver()
    yield driver
    driver.quit()

@pytest.mark.parametrize("data", test_data)
def test_search_data_driven(driver, data):
    search = SearchPage(driver)
    search.open()
    search.search_product(data["keyword"])

    results = search.get_results()

    if data["expected"] == "found":
        assert len(results) > 0
    else:
        assert len(results) == 0