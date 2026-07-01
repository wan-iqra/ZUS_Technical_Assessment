import allure

from config.constants import *

from pages.login_page import LoginPage


@allure.id("TC0002")
@allure.epic("SauceDemo")
@allure.feature("Authentication")
@allure.story("Invalid Login")
@allure.title("Login using an invalid password")
def test_invalid_login(driver):

    login = LoginPage(driver)

    login.login(USERNAME, INVALID_PASSWORD)

    assert "Username and password do not match any user in this service" in login.get_error()
