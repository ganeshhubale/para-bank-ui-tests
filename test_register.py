import fauxfactory

from utils import fill


def test_register_user(visitHost):
    """Test register new user"""
    newUser = fauxfactory.gen_alpha(4)

    driver = visitHost

    registerButton = driver.find_element_by_link_text("Register")
    registerButton.click()
    fill(driver, id="customer.firstName", value="TestUser")
    fill(driver, id="customer.lastName", value="TestUser")
    fill(driver, id="customer.address.street", value="A/P - Nangole")
    fill(driver, id="customer.address.city", value="Sangli")
    fill(driver, id="customer.address.state", value="Maharashtra")
    fill(driver, id="customer.address.zipCode", value="416405")
    fill(driver, id="customer.phoneNumber", value="1234567890")
    fill(driver, id="customer.ssn", value="123")
    fill(driver, id="customer.username", value=newUser)
    fill(driver, id="customer.password", value="test")
    fill(driver, id="repeatedPassword", value="test")
    registerEle = '//*[@id="customerForm"]//input[@value="Register"]'
    register = driver.find_element_by_xpath(registerEle)
    register.click()
    welcomeMsg = driver.find_element_by_xpath(".//h1")
    assert welcomeMsg.text == f"Welcome {newUser}"
