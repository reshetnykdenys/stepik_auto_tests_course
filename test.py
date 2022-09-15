from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:

    browser = webdriver.Chrome()

    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
    button = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )

    button = browser.find_element(By.ID, "book")
    button.click()
    browser.execute_script("window.scrollTo(0, 400)")
    option0 = browser.find_element(By.CSS_SELECTOR,"#input_value")
    x = option0.text
    y = calc(x)

    option1 = browser.find_element(By.CSS_SELECTOR,"#answer")
    option1.send_keys(y)
    option2 = browser.find_element(By.CSS_SELECTOR, "#solve")
    option2.click()









finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(3)
    # закрываем браузер после всех манипуляций
    browser.quit()
