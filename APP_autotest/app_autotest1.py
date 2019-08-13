
from appium import webdriver
from time import sleep

if __name__ == '__main__':
    des={}
    # 移动终端操作系统
    des['platformName'] = 'Android'
    # 移动终端设备
    des['deviceName'] = 'Android Emulator'
    # 运行APP
    des['app'] = r"f:\自动化测试学习\App\apks\ApiDemos-debug.apk"
    # 连接APPIUM ,打开APP
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',des)
    # 根据控件的文本（text）匹配控件
    driver.find_element_by_id('Accessibility').click()
    sleep(1)
    driver.find_element_by_id('Accessibility Node Provider').click()

    sleep(3)

    driver.quit()
