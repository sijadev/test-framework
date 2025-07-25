from selenium import webdriver

def create_driver():
    options = webdriver.SafariOptions()
    options.add_argument("--headless")  # optional
    driver = webdriver.Safari(options=options)
    driver.implicitly_wait(10)
    return driver