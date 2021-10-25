from selenium import webdriver
import time

import math

from selenium.webdriver.support.ui import Select

def calc(x,y):
  return str((int(x)+int(y)))

try: 
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_id("num1")
    y_element = browser.find_element_by_id("num2")

    result = calc(x_element.text, y_element.text)

    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(result) # ищем элемент с текстом "Python"

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(3)
    # закрываем браузер после всех манипуляций
    browser.quit()