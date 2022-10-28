from src.utils.android_actions import click_button_by_xpath, check_if_element_displayed_by_xpath
from appium.webdriver.common.appiumby import AppiumBy

class LoginScreen:

    def __init__(self, driver):
        self.driver = driver
        self.enter_number_button_xpath = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View[3]/android.view.View"
        self.login_screen_icon_xpath = "//android.widget.ImageView[@content-desc='mobile Number image']"
        self.enter_mobile_number_text_xpath = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View[2]/android.widget.TextView"
        self.mobile_number_field_xpath = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View[2]/android.view.View"

    def click_enter_number_button(self):
        click_button_by_xpath(self.driver, self.enter_number_button_xpath)
        return

    def check_login_screen_icon(self):
        return check_if_element_displayed_by_xpath(self.driver, self.login_screen_icon_xpath)

    def check_enter_mobile_number_text(self):
        return check_if_element_displayed_by_xpath(self.driver, self.enter_mobile_number_text_xpath)

    def check_mobile_number_field(self):
        return check_if_element_displayed_by_xpath(self.driver, self.mobile_number_field_xpath)



