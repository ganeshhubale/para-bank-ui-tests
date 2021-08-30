def fill(driver, id=None, name=None, value=None):
    """Fill input box"""
    if id:
        inputBox = driver.find_element_by_id(id)
    if name:
        inputBox = driver.find_element_by_name(name)
    inputBox.clear()
    inputBox.send_keys(value)
