
from typing import Any
from selenium.webdriver.safari.webdriver import WebDriver
from pages.login_page import LoginPage

def test_login_success(browser: WebDriver, test_data: Any):
    page = LoginPage(browser)
    page.login(test_data["username"], test_data["password"])
    assert "Log in to the site | New Site" in browser.title