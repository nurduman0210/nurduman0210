import pytest
from selenium import webdriver
import time
import math
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('webie', ["236895","236896","236897","236898", "236899", "236903","236904", "236905"])
def test_correct(browser, webie):
    link = f"https://stepik.org/lesson/{webie}/step/1"
    browser.get(link)
    answer = math.log(int(time.time()))
    input1 = WebDriverWait(browser, 5).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "[placeholder='Type your answer here...']"))
    )
    input1.send_keys(str(answer))
    button = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "submit-submission"))
    )
    button.click()
    feedback = WebDriverWait(browser, 5).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".smart-hints__hint"))
    )
    assert feedback.text == "Correct!", "Feedback option is not correct"

