from selenium import webdriver
import time
import math
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os 

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser.get(link)

    button1 = browser.find_element_by_css_selector("#book")
    WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
    button1.click()

    x_element = browser.find_element_by_id("input_value")
    browser.execute_script("return arguments[0].scrollIntoView(true);", x_element)
    
    x = x_element.text
    y = calc(x)

    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)

    button = browser.find_element_by_css_selector("#solve")
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()