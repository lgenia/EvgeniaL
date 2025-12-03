from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

class CheckoutCompletePage:
    def __init__(self, driver):
        self.driver = driver
    
    TOTAL_PRICE_LABEL = (By.CLASS_NAME, 'summary_total_label')

    def get_total_price(self):
        # Возвращает значение итоговой цены
        return self.driver.find_element(*self.TOTAL_PRICE_LABEL).text
