import os, sys
sys.path.insert(0, os.path.abspath(".."))

from pytest_bdd import scenarios, given, when, then, parsers
from src.utils.drivers import Driver
from src.Pages.android.SplashScreen import SplashScreen
from src.Pages.android.LoginScreen import LoginScreen
from src.Pages.android.PrivacyAndPolicy import PrivacyAndPolicy
from src.Pages.android.OTPScreen import OTPScreen
from src.Pages.android.TermsAndConditionsScreen import TermsAndConditions
from src.utils.android_actions import click_button_by_xpath, check_if_element_displayed_by_xpath, change_flight_mode_state
import time
scenarios("../../Features/android/LoginScreen.feature")

@given(u'The minimum Android OS version supporting BTLA OS 5 and above')
def initiate_connection(context):
    print("Initiate_connection")
    driver = Driver("android")
    context.driver = driver.get_driver()

@given(u'Launch the app online')
@when(u'Launch the app')
def launch_app(context):
    print("Launch App")
    splash_screen = SplashScreen(context.driver)
    splash_screen.click_location_permission_button()
    assert True

@when(u'Navigate to the Login screen')
@given(u'User is in Login screen')
def navigate_to_login_screen(context):
    print("Navigate to login screen")
    login_screen = LoginScreen(context.driver)
    login_screen.click_enter_number_button()
    assert True

@then(u'Verify that after launching the app, login screen should open in Portrait mode.')
def check_device_orientation(context):
    print("Check Device Orientation")
    assert context.driver.orientation == "PORTRAIT"

@then(u'Verify the Login screen icon')
@then(u'Verify that user should be redirected back to the Login screen')
def verify_login_screen_icon(context):
    print("Verify login screen icon")
    login_screen = LoginScreen(context.driver)
    assert login_screen.check_login_screen_icon()

@then(u'Verify the "Enter Mobile Number" text')
def verify_enter_mobile_number_text(context):
    print("Verify enter mobile number text")
    login_screen = LoginScreen(context.driver)
    assert login_screen.check_enter_mobile_number_text()

@then(u'Verify the Mobile Number field with auto-filled country code')
def verify_mobile_number_and_country_code(context):
    print("verify mobile number and auto filled country code")
    login_screen = LoginScreen(context.driver)
    assert login_screen.check_mobile_number_field() and login_screen.verify_auto_filled_country_code("+91")

@then(u'Verify the Send OTP button')
def verify_otp_button(context):
    print("verify otp button")
    login_screen = LoginScreen(context.driver)
    assert login_screen.check_send_otp_button()

@then(u"Verify the 'Privacy Policy and T&C' link")
def verify_privacy_policy_link(context):
    print("verify privacy policy link")
    context.driver.hide_keyboard()
    login_screen = LoginScreen(context.driver)
    login_screen.click_privacy_and_policy_link()
    privacy_screen = PrivacyAndPolicy(context.driver)
    assert privacy_screen.check_privacy_policy_header_text()

@given(u'Navigate to the Login screen')
def given_navigate_to_login_screen(context):
    navigate_to_login_screen(context)

@when(u'User taps on Country Code menu')
def click_country_code_menu(context):
    login_screen = LoginScreen(context.driver)
    login_screen.click_country_code_menu()
    assert True

@when(parsers.parse('select any from the bottom sheet {CountryCode:d}'))
def select_country_code(context, CountryCode):
    login_screen = LoginScreen(context.driver)
    login_screen.select_country_code_by_text(CountryCode)
    # login_screen.click_country_code_menu_cancel_button()
    assert True

@then(parsers.parse('Verify selected {CountryCode:d} should be shown in country code field'))
def verify_selected_country_code(context, CountryCode):
    print("verify selected country code field")
    login_screen = LoginScreen(context.driver)
    assert login_screen.verify_auto_filled_country_code("+" + str(CountryCode))

@when(u'User is in Country code bottom sheet dialog screen')
def check_country_code_menu(context):
    login_screen = LoginScreen(context.driver)
    assert login_screen.check_country_code_menu()

@when(u'user taps on Cancel button')
def click_cancel_counrty_code_menu(context):
    login_screen = LoginScreen(context.driver)
    login_screen.click_country_code_menu_cancel_button()
    assert True

@then(u'Verify that tapping on the Cancel button in the country code bottom sheet dialog, the bottom sheet should  dismiss from the screen i.e tapping outside the bottom sheet.')
def verify_country_code_is_dismissed(context):
    verify_otp_button(context)

@when(parsers.parse('Enters less than 7 digit Mobile Number {Digits:d}'))
def enter_mobile_number(context, Digits):
    login_screen = LoginScreen(context.driver)
    login_screen.send_keys("xpath", login_screen.mobile_number_field_xpath, "")
    login_screen.send_keys("xpath", login_screen.mobile_number_field_xpath, Digits)
    assert True

@then(u'Verify error message "Please enter valid mobile number" is displayed below mobile number field')
def verify_mobile_number_error_message(context):
    login_screen = LoginScreen(context.driver)
    assert login_screen.check_text("xpath", login_screen.mobile_number_error_message_xpath, "Please enter a valid mobile number")

@when(parsers.parse('Enter {Digits:d} above 15 in Mobile Number field with any'))
def enter_mobile_number_15_digits(context, Digits):
    enter_mobile_number(context, Digits)

@when(u'User enter a valid mobile number')
def enter_valid_mobile_number(context):
    # since mobile number will be prefilled by the app.
    enter_mobile_number(context, "")

@when(u'User taps on Send OTP')
def click_otp_button(context):
    login_screen = LoginScreen(context.driver)
    click_button_by_xpath(context.driver, login_screen.send_otp_button_view_xpath)
    assert True

@then(u'Verify that user is navigated to OTP Verification screen')
def verify_otp_screen_is_opened(context):
    otp_screen = OTPScreen(context.driver)
    assert check_if_element_displayed_by_xpath(context.driver, otp_screen.otp_field_xpath)

@when(u"User tap on the 'Privacy Policy' link")
def click_on_privacy_policy_link(context):
    context.driver.hide_keyboard()
    login_screen = LoginScreen(context.driver)
    login_screen.click_privacy_and_policy_link()
    assert True

@then(u'Verify that tapping on Privacy policy link in the login screen should navigate the user to the Privacy Policy screen')
@when(u'Verify the Privacy policy screen')
def check_if_privacy_page_is_opened(context):
    privacy_screen = PrivacyAndPolicy(context.driver)
    assert privacy_screen.check_privacy_policy_header_text()

@when(u'User taps on the app back arrow')
def click_on_back_arrow(context):
    privacy_screen = PrivacyAndPolicy(context.driver)
    privacy_screen.click_back_arrow_button()
    assert True

@when(u"User tap on the 'T & C' link")
def click_terms_page(context):
    context.driver.hide_keyboard()
    login_screen = LoginScreen(context.driver)
    login_screen.click_element("xpath", login_screen.terms_and_condition_xpath)
    assert True

@then(u'Verify that User should navigate to the Terms & Conditions screen')
def verify_terms_and_condition_page_is_opened(context):
    terms_and_condition_screen = TermsAndConditions(context.driver)
    assert terms_and_condition_screen.check_header_title()


@when(u'User enable offline mode')
def enable_offline_mode(context):
    print("enable offline mode")
    change_flight_mode_state(context.driver)
    assert True

@then(u'show offline mode')
def show_offline_mode(context):
    assert True