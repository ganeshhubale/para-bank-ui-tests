from utils import fill


def test_login_unsuccessful(visitHost):
    """Test log in with invalid creds"""
    driver = visitHost
    fill(driver, name="username", value="testUser")
    fill(driver, name="password", value="testPass")
    loginEle = '//div[@class="login"]/input[@class="button"]'
    loginButton = driver.find_element_by_xpath(loginEle)
    loginButton.click()
    errorMsg = driver.find_element_by_xpath("//*[@id='rightPanel']/p")
    assert "The username and password could not be verified." == errorMsg.text
