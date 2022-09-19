# import time
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium import webdriver
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.maximize_window()
# driver.get("https://practice.automationtesting.in/")
# time.sleep(1)
# my_account = driver.find_element_by_css_selector('[href="https://practice.automationtesting.in/my-account/"]')
# my_account.click()
# username = driver.find_element_by_id('username')
# username.send_keys('test.lgk@yandex.ru')
# password = driver.find_element_by_id("password")
# password.send_keys('testaccount2022')
# shop = driver.find_element_by_id('menu-item-40')
# shop.click()
# book = driver.find_element_by_css_selector('[href="https://practice.automationtesting.in/product/html5-forms/"]')
# book.click()
# book_name_check = WebDriverWait(driver, 30).until(
#     EC.text_to_be_present_in_element((By.CSS_SELECTOR, 'div.summary.entry-summary'), 'HTML5 Forms'))
# if book_name_check is True:
#     print('Книга называется "HTML5 Forms"')
# else:
#     print('Книга НЕ называется "HTML5 Forms"')

# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# import time
# from selenium.webdriver.common.by import By
# from selenium import webdriver
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.implicitly_wait(5)
# driver.maximize_window()
# driver.get("https://practice.automationtesting.in/")
# time.sleep(1)
# my_account = driver.find_element_by_css_selector('[href="https://practice.automationtesting.in/my-account/"]')
# my_account.click()
# username = driver.find_element_by_id('username')
# username.send_keys('test.lgk@yandex.ru')
# password = driver.find_element_by_id("password")
# password.send_keys('testaccount2022')
# shop = driver.find_element_by_id('menu-item-40')
# shop.click()
# html_page = driver.find_element_by_css_selector('[href="https://practice.automationtesting.in/product-category/html/"]')
# html_page.click()
# items_count = driver.find_elements(By.CSS_SELECTOR,'.product.type-product.status-publish.product_cat-html.product_tag-html')
# if len(items_count) == 3:
#     print("В корзине 3 товара")
# else:
#     print("Ошибка. Количество товаров в корзине: " + str(len(items_count)))

# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# import time
# from selenium.webdriver.support.select import Select
# from selenium import webdriver
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.implicitly_wait(5)
# driver.maximize_window()
# driver.get("https://practice.automationtesting.in/")
# time.sleep(1)
# my_account = driver.find_element_by_css_selector('[href="https://practice.automationtesting.in/my-account/"]')
# my_account.click()
# username = driver.find_element_by_id('username')
# username.send_keys('test.lgk@yandex.ru')
# password = driver.find_element_by_id("password")
# password.send_keys('testaccount2022')
# shop = driver.find_element_by_id('menu-item-40')
# shop.click()
# selector = driver.find_element_by_class_name('orderby')
# selector_value = selector.get_attribute("value")  # создали переменную, в которую поместим значение атрибута
# print("value of selector: ", selector_value)  # выводим в консоль значение атрибута
# if selector_value == 'menu_order':  # проверяем, если значение атрибута НЕ пустое, значит чекбокс отмечен
#     print("Сортировка по умолчанию")
# else:
#     print("Сортировка НЕ по умолчанию")
# selector_value = Select(selector)
# selector_value.select_by_value("price-desc")
# time.sleep(5)
# selector_new = driver.find_element_by_class_name('orderby')
# selector_value_new = selector_new.get_attribute("value")  # создали переменную, в которую поместим значение атрибута
# print("value of selector new: ", selector_value_new)  # выводим в консоль значение атрибута
# if selector_value_new == 'price-desc':  # проверяем, если значение атрибута НЕ пустое, значит чекбокс отмечен
#     print("Сортировка по цене")
# else:
#     print("Сортировка НЕ по цене")

# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# import time
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium import webdriver
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.maximize_window()
# driver.get("https://practice.automationtesting.in/")
# time.sleep(1)
# my_account = driver.find_element_by_css_selector('[href="https://practice.automationtesting.in/my-account/"]')
# my_account.click()
# username = driver.find_element_by_id('username')
# username.send_keys('test.lgk@yandex.ru')
# password = driver.find_element_by_id("password")
# password.send_keys('testaccount2022')
# shop = driver.find_element_by_id('menu-item-40')
# shop.click()
# book_one = driver.find_element_by_css_selector('[title="Android Quick Start Guide"]').click()
# book_price = driver.find_element_by_xpath('//*[@id="product-169"]/div[2]/div[1]/p/del/span')
# get_book_price = book_price.text
# print('старая цена =', get_book_price)
# assert get_book_price == "₹600.00"
# new_book_price = driver.find_element_by_xpath('//*[@id="product-169"]/div[2]/div[1]/p/ins/span')
# get_new_book_price = new_book_price.text
# print('новая цена =', get_new_book_price)
# assert get_new_book_price == "₹450.00"
# book_image = WebDriverWait(driver, 20).until(
# EC.element_to_be_clickable((By.CSS_SELECTOR, "[title='Android Quick Start Guide']")) )
# book_image.click()
# image_close = WebDriverWait(driver, 20).until(
#     EC.element_to_be_clickable((By.CLASS_NAME, "pp_close")))
# image_close.click()
# driver.quit()

# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# import time
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium import webdriver
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.maximize_window()
# driver.get("https://practice.automationtesting.in/")
# shop = driver.find_element_by_id('menu-item-40')
# shop.click()
# add_book = driver.find_element_by_css_selector('[href="/shop/?add-to-cart=182"]').click()
# time.sleep(4)
# cart_score = driver.find_element_by_class_name('cartcontents')
# get_cart_score = cart_score.text
# print('кол-во товаров в корзине =', get_cart_score)
# assert get_cart_score == "1 Item"
# cart_sum = driver.find_element_by_class_name('amount')
# get_cart_sum = cart_sum.text
# print('сумма товаров в корзине =', get_cart_sum)
# assert get_cart_sum == "₹180.00"
# cart = driver.find_element_by_id("wpmenucartli").click()
# time.sleep(4)
# subtotal_price = WebDriverWait(driver, 40).until(
# EC.text_to_be_present_in_element((By.CSS_SELECTOR, '[data-title="Subtotal"]'),"₹180.00") )
# total_price = WebDriverWait(driver, 40).until(
# EC.text_to_be_present_in_element((By.XPATH, '//*[@id="page-34"]/div/div[1]/div/div/table/tbody/tr[3]/td/strong/span'),"₹183.60") )
# driver.quit()

# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# import time
# from selenium import webdriver
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.maximize_window()
# driver.get("https://practice.automationtesting.in/")
# shop = driver.find_element_by_id('menu-item-40').click()
# driver.execute_script("window.scrollBy(0, 300);")
# add_book1 = driver.find_element_by_css_selector('[href="/shop/?add-to-cart=182"]').click()
# time.sleep(2)
# add_book2 = driver.find_element_by_css_selector('[href="/shop/?add-to-cart=180"]').click()
# cart = driver.find_element_by_id("wpmenucartli").click()
# delete_first_book = driver.find_element_by_css_selector('[data-product_id="182"]').click()
# time.sleep(2)
# undo_first_book = driver.find_element_by_css_selector('#page-34 > div > div.woocommerce > div.woocommerce-message > a')
# undo_first_book.click()
# book2_score = driver.find_element_by_css_selector('[max="9312"]')
# book2_score.clear()
# book2_score.click()
# book2_score.send_keys("3")
# update_cart = driver.find_element_by_css_selector('[name="update_cart"]').click()
# value_book2 = driver.find_element_by_css_selector('[max="9312"]')
# value_book2_num = value_book2.get_attribute("value")
# assert '3' in value_book2_num
# time.sleep(2)
# apply_coupon = driver.find_element_by_css_selector('[name="apply_coupon"]').click()
# time.sleep(2)
# text_element = driver.find_element_by_class_name("woocommerce-error")
# get_text_element = text_element.text
# assert "Please enter a coupon code." in get_text_element
# driver.quit()

# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# import time
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium import webdriver
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.maximize_window()
# driver.get("https://practice.automationtesting.in/")
# shop = driver.find_element_by_id('menu-item-40').click()
# driver.execute_script("window.scrollBy(0, 300);")
# add_book1 = driver.find_element_by_css_selector('[href="/shop/?add-to-cart=182"]').click()
# time.sleep(2)
# cart = driver.find_element_by_id("wpmenucartli").click()
# proceed_to_checkout_btn = WebDriverWait(driver, 20).until(
#      EC.element_to_be_clickable((By.CSS_SELECTOR, '[href="https://practice.automationtesting.in/checkout/"]')))
# proceed_to_checkout_btn.click()
# first_name = WebDriverWait(driver, 20).until(
#     EC.element_to_be_clickable((By.ID, "billing_first_name")))
# first_name.send_keys('Test')
# last_name = driver.find_element_by_id('billing_last_name')
# last_name.send_keys('Testing')
# email = driver.find_element_by_id('billing_email')
# email.send_keys('test.lgk@yandex.ru')
# phone = driver.find_element_by_id('billing_phone')
# phone.send_keys('+79991234567')
# country = driver.find_element_by_id('select2-chosen-1').click()
# country_enter = driver.find_element_by_id('s2id_autogen1_search')
# country_enter.send_keys('Russia')
# country_choice = driver.find_element_by_class_name('select2-match').click()
# address = driver.find_element_by_id('billing_address_1')
# address.send_keys('myaddress')
# city = driver.find_element_by_id('billing_city')
# city.send_keys('Saint-P')
# state = driver.find_element_by_id('billing_state')
# state.send_keys('Saint-P')
# postcode = driver.find_element_by_id('billing_postcode')
# postcode.send_keys('199833')
# driver.execute_script("window.scrollBy(0, 600);")
# time.sleep(2)
# check_payments = driver.find_element_by_id('payment_method_cheque').click()
# place_order = driver.find_element_by_id('place_order').click()
# text = WebDriverWait(driver, 20).until(
#     EC.text_to_be_present_in_element((By.CLASS_NAME, "woocommerce-thankyou-order-received"), 'Thank you. Your order has been received.'))
# payment_method = WebDriverWait(driver, 20).until(
#     EC.text_to_be_present_in_element((By.CLASS_NAME, "method"), 'Check Payments'))
# driver.quit()
