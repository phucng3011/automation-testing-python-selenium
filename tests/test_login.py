import pytest
from utils.driver_factory import get_driver
from pages.login_page import LoginPage

@pytest.fixture
def driver():
    driver = get_driver()
    yield driver
    driver.quit()

def test_login_success(driver):
    login = LoginPage(driver)
    login.open()
    login.login("Admin", "admin123")
    assert login.is_login_successful()

def test_login_invalid_password(driver):
    login = LoginPage(driver)
    login.open()
    login.login("Admin", "wrongpass")
    assert not login.is_login_successful()

def test_login_empty_fields(driver):
    login = LoginPage(driver)
    login.open()
    login.login("", "")
    assert "login" in driver.current_url