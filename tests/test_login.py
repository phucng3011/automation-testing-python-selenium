import pytest
from utils.driver_factory import get_driver
from pages.login_page import LoginPage
from utils.data_reader import load_test_data

test_data = load_test_data("data/testdata.json")["login"]

@pytest.fixture
def driver():
    driver = get_driver()
    yield driver
    driver.quit()

@pytest.mark.parametrize("data", test_data)
def test_login_data_driven(driver, data):
    login = LoginPage(driver)
    login.open()
    login.login(data["username"], data["password"])

    if data["expected"] == "success":
        assert login.is_login_successful()
    else:
        assert not login.is_login_successful()