from appium.webdriver.common.appiumby import AppiumBy
from src.utils.android_actions import click_button_by_id

class SplashScreen:

    def __init__(self, driver):

        self.driver = driver

        self.location_permission_button_id = "com.android.permissioncontroller:id/permission_allow_foreground_only_button"

    def click_location_permission_button(self):
        click_button_by_id(self.driver, self.location_permission_button_id)
        return


