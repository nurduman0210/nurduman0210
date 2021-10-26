from selenium import webdriver
import time

link = "http://suninjuly.github.io/registration2.html"
browser = webdriver.Chrome()
browser.get(link)

import unittest

class TestAbs(unittest.TestCase):
    def test_abs1(self):
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "They should be equal")
    
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # # закрываем браузер после всех манипуляций
    browser.quit()

    # Ваш код, который заполняет обязательные поля

input1 = browser.find_element_by_css_selector("[placeholder='Input your first name']")
input1.send_keys("Ivan")
input2 = browser.find_element_by_css_selector("[placeholder='Input your last name']")
input2.send_keys("Petrov")
input3 = browser.find_element_by_css_selector("[placeholder='Input your email']")
input3.send_keys("Smolensk@p.com")

# Отправляем заполненную форму
button = browser.find_element_by_css_selector("button.btn")
button.click()

# Проверяем, что смогли зарегистрироваться
# ждем загрузки страницы
time.sleep(1)


# находим элемент, содержащий текст
welcome_text_elt = browser.find_element_by_tag_name("h1")
# записываем в переменную welcome_text текст из элемента welcome_text_elt
welcome_text = welcome_text_elt.text

if __name__ == "__main__":
    unittest.main()