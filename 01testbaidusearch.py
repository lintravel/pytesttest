from selenium import webdriver
import time
driver = webdriver.Chrome(executable_path="./chromedriver.exe")
driver.get("http://132.232.44.158:7777/sign?")

#driver.find_element_by_id("kw").send_keys("软件测试")
time.sleep(3)

driver.find_element_by_xpath("/html/body/div/form/button").click()
#driver.find_element_by_id("su").click()
title = driver.title

if title == "欢迎回来":
    print("签到成功")
else:
    print("failue")

driver.quit()
    