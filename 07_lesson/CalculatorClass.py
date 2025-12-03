import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver
    
    # Локаторы элементов
    DELAY_INPUT_LOCATOR = (By.ID, 'delay')
    SCREEN_OUTPUT_LOCATOR = (By.CLASS_NAME, 'screen')
    BUTTONS_XPATH_TEMPLATE = "//span[text()='%s']"

    def open(self):
        # Открывает страницу калькулятора
        self.driver.get('https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html')

    def set_delay(self, value: str):
        # Устанавливает задержку
        input_field = self.driver.find_element(*self.DELAY_INPUT_LOCATOR)
        input_field.clear()
        input_field.send_keys(value)

    def click_button(self, text: str):
        # Нажимает указанную кнопку
        button_xpath = self.BUTTONS_XPATH_TEMPLATE % text
        button = self.driver.find_element(By.XPATH, button_xpath)
        button.click()

    def wait_for_result(self, timeout: int):
        # Ожидает появление результата
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(self.SCREEN_OUTPUT_LOCATOR))

    def get_screen_value(self) -> str:
        # Возвращает текущее значение поля вывода результатов"""
        screen_output = self.driver.find_element(*self.SCREEN_OUTPUT_LOCATOR)
        return screen_output.text.strip()