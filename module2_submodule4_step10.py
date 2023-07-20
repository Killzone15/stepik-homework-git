import time
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver


def calc(x_fun):
    return str(math.log(abs(12 * math.sin(int(x_fun)))))


try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, 'price'), '$100'))

    book_button = browser.find_element(By.ID, 'book')
    book_button.click()

    x = browser.find_element(By.ID, 'input_value').text
    y = calc(x)

    answer = browser.find_element(By.ID, 'answer')
    answer.send_keys(y)

    submit_button = browser.find_element(By.ID, 'solve')
    submit_button.click()

finally:
    time.sleep(5)
    browser.quit()
