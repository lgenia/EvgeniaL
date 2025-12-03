from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

class CartPage:
    def __init__(self, driver):
        self.driver = driver
    
    CHECKOUT_BUTTON = (By.ID, 'checkout')

    def checkout(self):
        # Инициализирует оформление заказа
        checkout_btn = self.driver.find_element(*self.CHECKOUT_BUTTON)
        checkout_btn.click()
