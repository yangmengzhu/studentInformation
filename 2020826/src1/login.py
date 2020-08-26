import time

from selenium import webdriver

driver=webdriver.Chrome()
driver.get("http://localhost:8080/sis/public/index.html")
driver.maximize_window()
time.sleep(3)
driver.find_element_by_xpath("//*[@id='login_form']/div[2]/div/input").send_keys("abc")
time.sleep(3)
driver.find_element_by_xpath("//*[@id='login_form']/div[3]/div/input").send_keys("123")
time.sleep(3)
driver.find_element_by_xpath("//*[@id='login_form']/div[6]/input[2]").click()
time.sleep(10)
driver.quit()