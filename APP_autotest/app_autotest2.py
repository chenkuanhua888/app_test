from appium import webdriver
from time import sleep

if __name__ == '__main__':

    desired_caps = {}

    desired_caps['platformName'] = 'Android'
    desired_caps['deviceName'] = 'Android Emulator'

    desired_caps['app'] = r"f:\自动化测试学习\App\apks\ApiDemos-debug.apk"

    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)
    # driver.find_element_by_id('Accessibility').click()

    # driver.find_element_by_accessibility_id('Accessibility').click()
    # sleep(2)
    # driver.quit()

    ele = driver.find_elements_by_class_name('android.widget.TextView')
    print(type(ele))
    print(len(ele))
    ele[1].click()


    sleep(1)
    driver.quit()