from test_framework.pages.login_page import LoginPage

def open_login_page(driver):
    page = LoginPage(driver)
    page.open()

def login_as_user(driver, username, password):
    page = LoginPage(driver)
    page.login(username, password)

def verify_dashboard(driver):
    page = LoginPage(driver)
    assert page.is_dashboard_visible(), "Dashboard ist nicht sichtbar"