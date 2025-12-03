from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

class CheckoutStepOnePage:
    def __init__(self, driver):
        self.driver = driver
    
    FIRST_NAME_FIELD = (By.ID, 'first-name')
    LAST_NAME_FIELD = (By.ID, 'last-name')
    POSTAL_CODE_FIELD = (By.ID, 'postal-code')
    CONTINUE_BUTTON = (By.ID, 'continue')

    def fill_personal_data(self, first_name, last_name, postal_code):
        # Заполняет персональные данные клиента
        first_field = self.driver.find_element(*self.FIRST_NAME_FIELD)
        first_field.send_keys(first_name)
        
        last_field = self.driver.find_element(*self.LAST_NAME_FIELD)
        last_field.send_keys(last_name)
        
        post_field = self.driver.find_element(*self.POSTAL_CODE_FIELD)
        post_field.send_keys(postal_code)
    
    def continue_checkout(self):
        # Продолжает оформление заказа
        cont_btn = self.driver.find_element(*self.CONTINUE_BUTTON)
        cont_btn.click()
