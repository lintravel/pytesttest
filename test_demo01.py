'''
环境配置：pip install pytest

运行：1、pytest xxx.py
	2、pytest pytesttest/  #所有py文件都是以test_开头

测试结果的状态：1、.通过
		  2、F失败，断言失败
		   3、E错误，代码错误

测试报告allure：1、安装配置allure-commandline环境变量
		2、pip install allure-pytest
		3、修改pytest运行命令  pytest xxx.py --alluredir result
		4、测试结果转网页allure generate ./result -o ./report_html --clean
		5、打开测试报告allure open -h 127.0.0.1 -p 9999 ./report_html  

'''

import pytest
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

class TestCaseTests():

    def test_selenium(self):

        driver = webdriver.Chrome(executable_path="E:\\seleniumstdy\\chromedriver.exe")
        driver.get("https://www.baidu.com")

        driver.find_element_by_id("kw").send_keys("软件测试")
        time.sleep(3)

        driver.find_element_by_id("su").click()
        title = driver.title
        time.sleep(3)
        assert title=="软件测试_百度搜索"
        driver.quit()
