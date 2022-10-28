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
