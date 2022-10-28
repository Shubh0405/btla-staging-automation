import os, sys
sys.path.insert(0, os.path.abspath(".."))

from pytest_bdd import *
from src.utils.drivers import Driver
from src.Pages.android.SplashScreen import SplashScreen
from src.Pages.android.LoginScreen import LoginScreen

scenarios("../../Features/android/LoginScreen.feature")

@given(u'The minimum Android OS version supporting BTLA OS 5 and above')
def initiate_connection(context):
    print("Initiate_connection")
    driver = Driver("android")
    context.driver = driver.get_driver()

@given(u'Launch the app online')
def launch_app1(context):
    print("Launch App1")
    splash_screen = SplashScreen(context.driver)
    splash_screen.click_location_permission_button()
    assert True

@when(u'Launch the app')
def launch_app(context):
    print("Launch App")
    splash_screen = SplashScreen(context.driver)
    splash_screen.click_location_permission_button()
    assert True

@when(u'Navigate to the Login screen')
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
def verify_login_screen_icon(context):
    print("Verify login screen icon")
    login_screen = LoginScreen(context.driver)
    assert login_screen.check_login_screen_icon()
