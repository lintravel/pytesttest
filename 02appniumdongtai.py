from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time

def get_driver(pv='5.1.1',dn='huawei Honor V9',ap='io.appium.android.apis',aa='.ApiDemos'):
    devicescaps = {}
    devicescaps['platformName'] = 'Android'                    
    devicescaps['platformVersion'] = pv                
    devicescaps['deviceName'] = dn             
    devicescaps['appPackage'] = ap      
    devicescaps['appActivity'] = aa                  
    devicescaps['unicodeKeyboard'] = True                      
    devicescaps['resetKeyboard'] = True                        

    # 去打开app，并且返回当前app的操作对象
    driver = webdriver.Remote('http://localhost:4723/wd/hub', devicescaps)
    return driver

def find_element(driver,locator):
    try:
        return WebDriverWait(driver,30).until(lambda s:s.find_element(*locator))
    except:
        raise Exception("未找到元素{}".format(locator))
    

def c(driver,locator):#二次封装
    find_element(driver,locator).click()

'''
id:id->resource id
xpath:xpath
accessibility_id:accessibility id  ->content desc
android_uiautomator:-android uiautomator->text
'''
if __name__=='__main__':
    driver = get_driver()
    locator1=('id','android:id/text1')
    locator2=('accessibility id','Animation')
    locator3=('-android uiautomator','new UiSelector().text("App")')
    locator4=('accessibility id','Menu')
    c(driver,locator1)
    driver.back()
    c(driver,locator2)
    driver.back()
    c(driver,locator3)
    c(driver,locator4)
    driver.press_keycode(3)
    time.sleep(5)
    for i in range(30):
        driver.swipe(480,500,1000,500)



    
 
