import time

from selenium import webdriver
from selenium.webdriver import ActionChains

driver=webdriver.Chrome()
driver.get("http://localhost:8080/sis/public/page/main.html")
driver.maximize_window()
driver.implicitly_wait(5)
driver.find_element_by_xpath("//*[@id='login_form']/div[2]/div/input").send_keys("abc")
time.sleep(3)
driver.find_element_by_xpath("//*[@id='login_form']/div[3]/div/input").send_keys("123")
time.sleep(3)
driver.find_element_by_xpath("//*[@id='login_form']/div[6]/input[2]").click()
driver.implicitly_wait(10)
div=driver.find_element_by_class_name("modal-footer")
div.find_element_by_xpath("//*[@id='main_fail_modal_dialog']/div/div[3]/button").click()
driver.implicitly_wait(5)
target=driver.find_element_by_xpath("//*[@id='stu_table']/tbody/tr[1]/td[4]")
ActionChains(driver).move_to_element(target).perform()
driver.implicitly_wait(5)
div2=driver.find_element_by_xpath("//*[@id='stu_panel']/div[1]/div[1]")
driver.implicitly_wait(5)
div2.find_element_by_id("stu_table_toolbar_delete").click()
div3=driver.find_element_by_xpath("//*[@id='stu_table_toolbar_delete_confirm_modal']/div/div/div[3]")
driver.implicitly_wait(5)
div3.find_element_by_xpath("//*[@id='stu_table_toolbar_delete_confirm_modal_submit']").click()
driver.implicitly_wait(5)
driver.quit()