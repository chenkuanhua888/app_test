
from time import sleep
from appium import webdriver
import os
import unittest
import warnings



if __name__ == '__main__':

        warnings.filterwarnings('ignore')
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['deviceName'] = 'Android Emulator'
        desired_caps['app'] = r"F:\自动化测试学习\App\apks\ApiDemos-debug.apk"

        driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

        driver.find_element_by_id('Accessibility').click()

        driver.find_element_by_id('Accessibility Node Provider').click()

        sleep(2)
        driver.quit()





