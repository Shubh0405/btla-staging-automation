from appium import webdriver as appium_driver


class Driver:

    def __init__(self, platform):

        if platform == "android":

            desired_cap = {
              "platformName": "Android",
              "appium:uiautomator2ServerInstallTimeout": "90000",
              "appium:deviceName": "RZCT609NGNJ",
              "appium:appPackage": "com.byjus.thelearningapp",
              "appium:appActivity": "com.byjus.app.onboarding.activity.SplashActivity"
            }

            self.driver = appium_driver.Remote("http://127.0.0.1:4723/wd/hub", desired_cap)
            self.driver.implicitly_wait(15)

        elif platform == "web":
            raise NotImplementedError("Driver for web platform is not implemented yet!")
        elif platform == "ios":
            raise NotImplementedError("Driver for ios platform is not implemented yet!")
        else:
            raise NotImplementedError("Platform name not recognized!")

    def get_driver(self):
        return self.driver

    def get_device_orientation(self):
        return self.driver.orientation
