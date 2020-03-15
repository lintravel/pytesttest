from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
import unittest

class TestCaseShop(unittest.TestCase):                                                      #申明class继承unittest.TestCase方法

    def test_01_shop1(self):
        '''
        这是第一个测试用例。。。

        '''
        driver=webdriver.Chrome(executable_path="E:\\seleniumstdy\\chromedriver.exe")
        driver.get("http://132.232.44.158:8080/")
        sleep(3)

        driver.find_element_by_xpath('//*[@id="J_wrap_pro_add"]/li[2]/div[1]/a/img').click() #通过xpath找到商品并点击该商品（芥兰）
        sleep(3)
        driver.find_element_by_xpath('//*[@id="J_mer_saleTag"]').click()                     #通过xpath找到加入购物袋按钮并点击该按钮
        sleep(3)
        driver.find_element_by_xpath('//*[@id="J_header_cart"]/div[1]/a[1]').click()         #通过xpath找到购物袋并点击购物袋
        sleep(3)
        e=driver.find_elements_by_link_text("芥兰")                                          #通过link_text查找商品芥兰

        self.assertNotEqual(len(e),0)                                                        #断言商品是否存在

        driver.quit()                                                                        #退出浏览器
    
    def test_02_shop2(self):
        '''
        这是第二个测试用例。。。
        '''
        driver=webdriver.Chrome(executable_path="E:\\seleniumstdy\\chromedriver.exe")
        driver.get("http://132.232.44.158:8080/")

        baicaitai=('xpath','//*[@id="J_wrap_pro_add"]/li[3]/div[1]/a/img')
        ee=WebDriverWait(driver,10).until(lambda s : s.find_element(*baicaitai))
        ee.click()
        jiagou=('id','J_mer_saleTag')
        e1=WebDriverWait(driver,10).until(lambda s : s.find_element(*jiagou))
        e1.click()
        bag=('link text',"购物袋")
        e2=WebDriverWait(driver,10).until(lambda s : s.find_element(*bag))
        e2.click()
        #baicaitai1=('xpath','//*[@id="cart_item_3"]/td[1]/a/img')
        #e3=WebDriverWait(driver,10).until(lambda s : s.find_element(*baicaitai1))
        e=driver.find_element_by_link_text("白菜苔")

        self.assertNotEqual(len(e),0)

        driver.quit()
      
if __name__=="__main__":
    unittest.main()