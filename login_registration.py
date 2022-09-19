# import time
# from selenium import webdriver
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.get("https://practice.automationtesting.in/")
# time.sleep(3)
# my_account = driver.find_element_by_css_selector('[href="https://practice.automationtesting.in/my-account/"]')
# my_account.click()
# email = driver.find_element_by_id('reg_email')
# email.send_keys('test.lgk@yandex.ru')
# password = driver.find_element_by_id("reg_password")
# password.send_keys('testaccount2022')
# register_btn = driver.find_element_by_name("register")
# register_btn.click()

# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

import time
from selenium import webdriver
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.get("https://practice.automationtesting.in/")
time.sleep(3)
my_account = driver.find_element_by_css_selector('[href="https://practice.automationtesting.in/my-account/"]')
my_account.click()
username = driver.find_element_by_id('username')
username.send_keys('test.lgk@yandex.ru')
password = driver.find_element_by_id("password")
password.send_keys('testaccount2022')
login_btn = driver.find_element_by_name("login")
login_btn.click()
logout_btn = driver.find_element_by_class_name("woocommerce-MyAccount-navigation-link--customer-logout")
element_logout_btn = logout_btn.text
assert "Logout" in element_logout_btn
driver.quit()