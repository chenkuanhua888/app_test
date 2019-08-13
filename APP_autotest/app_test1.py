
from time import sleep
from appium import webdriver
import os
import unittest
import warnings


class SimpleAndroidTests(unittest.TestCase):


    def setUp(self):
        warnings.filterwarnings('ignore')
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['deviceName'] = 'Android Emulator'
        desired_caps['app'] = r"F:\自动化测试学习\App\apks\ApiDemos-debug.apk"

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def tearDown(self):
        # sleep(2)
        self.driver.quit()

    def test_simple_actions(self):
        ele =self.driver.find_element_by_accessibility_id('Graphics')
        ele.click()
        ele = self.driver.find_element_by_accessibility_id('Arcs')
        ele.click()
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("Graphics/Arcs")')


if __name__ == '__main__':

    suite = unittest.TestLoader().loadTestsFromTestCase(SimpleAndroidTests)
    unittest.TextTestRunner(verbosity=2).run(suite)


