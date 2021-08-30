import pytest
from selenium import webdriver


@pytest.fixture(scope="module")
def visitHost():
    """Fixture to visit host"""
    driver = webdriver.Firefox()
    driver.get("https://parabank.parasoft.com")
    yield driver
    driver.close()
