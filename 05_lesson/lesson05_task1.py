# Открыть браузер Google Chrome.
# Перейти на страницу: http://uitestingplayground.com/classattr.
# Кликнуть на синюю кнопку.

from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(
    service=ChromeService(
        ChromeDriverManager().install()))
driver.get("http://uitestingplayground.com/classattr")
check_input = driver.find_element(By.CSS_SELECTOR, ".btn-primary")
check_input.click()

sleep(2)
