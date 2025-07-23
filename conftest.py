# filepath: conftest.py
import pytest
import yaml
from selenium import webdriver

@pytest.fixture
def browser():
    driver = webdriver.Safari()
    yield driver
    driver.quit()

@pytest.fixture
def test_data():
    with open("data/login_data.yaml") as f:
        return yaml.safe_load(f) 