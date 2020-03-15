from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time
def get_driver():
    desired_caps = {}
    desired_caps['platformName'] = 'Android'                    # 打开什么平台的app，固定的 > 启动安卓平台
    desired_caps['platformVersion'] = '5.1.1'                   # 安卓系统的版本号：adb shell getprop ro.build.version.release
    desired_caps['deviceName'] = 'huawei Honor V9'              # 手机/模拟器的型号：adb shell getprop ro.product.model
    desired_caps['appPackage'] = 'io.appium.android.apis'       # app的名字：adb shell dumpsys activity | findstr "mFocusedActivity"
    desired_caps['appActivity'] = '.ApiDemos'                   # app的启动页名字：adb shell dumpsys activity | findstr "mFocusedActivity"
    desired_caps['unicodeKeyboard'] = True                      # 为了支持中文
    desired_caps['resetKeyboard'] = True                        # 设置成appium自带的键盘

    # 去打开app，并且返回当前app的操作对象
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    return driver
def test():
    driver=get_driver()
    
    driver.find_element_by_id('android:id/text1').click()       #通过id查找元素
    driver.back()
    driver.find_element_by_android_uiautomator('new UiSelector().text("Content")').click()  #通过文本值查找元素
    driver.back()
    driver.find_element_by_accessibility_id('Animation').click()   #通过content-desc查找元素          
    driver.back()
    driver.find_element_by_xpath('//android.widget.TextView[@content-desc="App"]').click()#通过xpath查找元素
    driver.back()
    locator=("xpath",'//android.widget.TextView[@content-desc="Animation"]')#动态查找元素
    WebDriverWait(driver,30).until(lambda s:s.find_element(*locator)).click()

    driver.quit()
    
if __name__=="__main__":
    test()


