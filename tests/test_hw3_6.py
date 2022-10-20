import time
import math
import pytest
from selenium.webdriver.common.by import By



@pytest.mark.parametrize('link', [
    "https://stepik.org/lesson/236895/step/1",
    "https://stepik.org/lesson/236896/step/1",
    "https://stepik.org/lesson/236897/step/1",
    "https://stepik.org/lesson/236898/step/1",
    "https://stepik.org/lesson/236899/step/1",
    "https://stepik.org/lesson/236903/step/1",
    "https://stepik.org/lesson/236904/step/1",
    "https://stepik.org/lesson/236905/step/1",
])
def test_guest_should_see_login_link(browser, link):
    link = f"{link}"
    browser.implicitly_wait(10)
    browser.get(link)
    element = browser.find_element(By.CSS_SELECTOR, ".ember-text-area.ember-view.textarea.string-quiz__textarea")
    element.click()
    answer = math.log(int(time.time()))
    element.send_keys(answer)
    element1 = browser.find_element(By.CSS_SELECTOR, ".submit-submission")
    element1.click()
    browser.implicitly_wait(10)
    element2 = browser.find_element(By.CSS_SELECTOR, ".smart-hints__hint")
    element3 = element2.text
    assert element3 == "Correct!"
    browser.implicitly_wait(10)