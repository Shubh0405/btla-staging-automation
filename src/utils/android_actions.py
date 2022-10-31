from appium.webdriver.common.appiumby import AppiumBy


def click_button_by_id(driver, appium_id):
    driver.find_element(AppiumBy.ID, appium_id).click()
    return

def click_button_by_xpath(driver, appium_xpath):
    driver.find_element(AppiumBy.XPATH, appium_xpath).click()
    return

def check_if_element_displayed_by_xpath(driver, appium_xpath):
    return driver.find_element(AppiumBy.XPATH, appium_xpath).is_displayed()

def check_if_element_displayed_by_id(driver, appium_id):
    return driver.find_element(AppiumBy.ID, appium_id).is_displayed()

def get_element_text_by_xpath(driver, appium_xpath):
    return driver.find_element(AppiumBy.XPATH, appium_xpath).text

def get_element_text_by_id(driver, appium_id):
    return driver.find_element(AppiumBy.ID, appium_id).text

def send_keys_by_xpath(driver, appium_xpath, keys):
    driver.find_element(AppiumBy.XPATH, appium_xpath).send_keys(keys)

def send_keys_by_id(driver, appium_id, keys):
    driver.find_element(AppiumBy.ID, appium_id).send_keys(keys)
