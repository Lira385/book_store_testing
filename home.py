import time
from selenium import webdriver
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.get("http://practice.automationtesting.in/")
time.sleep(1)
driver.execute_script("window.scrollBy(0, 600);")
book_name = driver.find_element_by_css_selector('[href="https://practice.automationtesting.in/product/selenium-ruby/"]')
book_name.click()
reviews = driver.find_element_by_css_selector('[href="#tab-reviews"]')
reviews.click()
stars = driver.find_element_by_css_selector('[class="star-5"]')
stars.click()
comment = driver.find_element_by_id('comment')
comment.send_keys("Nice book!")
name = driver.find_element_by_id("author")
name.send_keys('Lira')
e_mail = driver.find_element_by_id("email")
e_mail.send_keys('1234@gmail.com')
send_btn = driver.find_element_by_css_selector('[name="submit"]')
send_btn.click()