from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
import time

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
    print(appium_xpath)
    print(driver.find_element(AppiumBy.XPATH, appium_xpath).text)
    return driver.find_element(AppiumBy.XPATH, appium_xpath).text

def get_element_text_by_id(driver, appium_id):
    return driver.find_element(AppiumBy.ID, appium_id).text

def send_keys_by_xpath(driver, appium_xpath, keys):
    driver.find_element(AppiumBy.XPATH, appium_xpath).send_keys(keys)

def send_keys_by_id(driver, appium_id, keys):
    driver.find_element(AppiumBy.ID, appium_id).send_keys(keys)

def change_flight_mode_state(driver):
    deviceSize = driver.get_window_size()

    screenWidth = deviceSize['width']
    screenHeight = deviceSize['height']

    print(screenHeight, screenWidth)

    startx = 554
    endx = 529
    endy = 2146
    starty = 14

    # startx = 0
    # endx = 0
    # starty = 1.0
    # endy = 0

    actions = TouchAction(driver)

    for i in range(2):
        print("swipe done")
        actions.long_press(None, startx, starty).move_to(None, endx, endy).release().perform()

    driver.find_element(AppiumBy.XPATH, "//android.view.ViewGroup[@content-desc='Flight,mode,Off.,Button']").click()
    time.sleep(10)

    for i in range(2):
        print("reverse swipe done")
        actions.long_press(None, endx, endy).move_to(None, startx, starty).release().perform()

    return

