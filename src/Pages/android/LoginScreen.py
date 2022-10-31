from src.utils.android_actions import click_button_by_xpath, check_if_element_displayed_by_xpath, check_if_element_displayed_by_id, \
    get_element_text_by_xpath, send_keys_by_xpath, send_keys_by_id, get_element_text_by_id, click_button_by_id
from appium.webdriver.common.appiumby import AppiumBy


class LoginScreen:

    def __init__(self, driver):
        self.driver = driver
        self.enter_number_button_xpath = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View[3]/android.view.View"
        self.login_screen_icon_xpath = "//android.widget.ImageView[@content-desc='mobile Number image']"
        self.enter_mobile_number_text_xpath = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View[2]/android.widget.TextView"
        self.mobile_number_view_xpath = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View[2]/android.view.View"
        self.mobile_number_field_xpath = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.widget.EditText"
        self.country_code_field_xpath = "//android.view.View[@content-desc='country code field']/android.widget.TextView"
        self.send_otp_button_view_xpath = "//android.view.View[@content-desc='Send OTP button']"
        self.privacy_and_policy_link_xpath = "//android.widget.TextView[@content-desc='Privacy Policy']"
        self.terms_and_condition_xpath = "//android.widget.TextView[@content-desc='T&C']"
        self.country_code_menu_xpath = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.view.View"
        self.country_code_menu_cancel_button_xpath = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.view.View/android.view.View[1]"
        self.mobile_number_error_message_xpath = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.widget.TextView"

    def click_enter_number_button(self):
        click_button_by_xpath(self.driver, self.enter_number_button_xpath)
        return

    def check_login_screen_icon(self):
        return check_if_element_displayed_by_xpath(self.driver, self.login_screen_icon_xpath)

    def check_enter_mobile_number_text(self):
        return check_if_element_displayed_by_xpath(self.driver, self.enter_mobile_number_text_xpath)

    def check_mobile_number_field(self):
        return check_if_element_displayed_by_xpath(self.driver, self.mobile_number_view_xpath)

    def verify_auto_filled_country_code(self, country_code):
        print(country_code)
        return get_element_text_by_xpath(self.driver, self.country_code_field_xpath) == country_code

    def check_send_otp_button(self):
        return check_if_element_displayed_by_xpath(self.driver, self.send_otp_button_view_xpath)

    def click_privacy_and_policy_link(self):
        click_button_by_xpath(self.driver, self.privacy_and_policy_link_xpath)
        return

    def click_country_code_menu(self):
        click_button_by_xpath(self.driver, self.country_code_field_xpath)
        return

    def select_country_code_by_text(self, text):
        element_xpath = "//android.widget.TextView[@text='+{temp_text}']".format(temp_text=text)
        print(element_xpath)
        click_button_by_xpath(self.driver,element_xpath)
        return

    def click_country_code_menu_cancel_button(self):
        click_button_by_xpath(self.driver, self.country_code_menu_cancel_button_xpath)
        return

    def check_country_code_menu(self):
        return check_if_element_displayed_by_xpath(self.driver, self.country_code_menu_xpath)

    def check_element(self, path_type, path_value):
        if path_type == "xpath":
            check_if_element_displayed_by_xpath(self.driver, path_value)
        else:
            check_if_element_displayed_by_id(self.driver, path_value)

    def send_keys(self, path_type, path_value, keys):
        if path_type == "xpath":
            send_keys_by_xpath(self.driver, path_value, keys)
        else:
            send_keys_by_id(self.driver, path_value, keys)

    def check_text(self, path_type, path_value, text):
        if path_type == "xpath":
            return get_element_text_by_xpath(self.driver, path_value) == text
        else:
            return get_element_text_by_id(self.driver, path_value) == text

    def click_element(self, path_type, path_value):
        if path_type == "xpath":
            click_button_by_xpath(self.driver, path_value)
        else:
            click_button_by_id(self.driver, path_value)
        return
