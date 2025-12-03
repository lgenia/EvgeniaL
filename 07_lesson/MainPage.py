from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

class MainPage:
    def __init__(self, driver):
        self.driver = driver
        
    # Локаторы элементов
    CART_LINK = (By.CLASS_NAME, 'shopping_cart_link')
    ADD_TO_CART_BUTTON = {
        "Sauce Labs Backpack": (By.XPATH, "//div[text()='Sauce Labs Backpack']/ancestor::div[@class='inventory_item']//button"),
        "Sauce Labs Bolt T-Shirt": (By.XPATH, "//div[text()='Sauce Labs Bolt T-Shirt']/ancestor::div[@class='inventory_item']//button"),
        "Sauce Labs Onesie": (By.XPATH, "//div[text()='Sauce Labs Onesie']/ancestor::div[@class='inventory_item']//button")
    }

    def add_items_to_cart(self, *items):
        # Метод добавляет указанные товары в корзину
        for item in items:
            if item in self.ADD_TO_CART_BUTTON:
                button = self.driver.find_element(*self.ADD_TO_CART_BUTTON[item])
                button.click()
                
    def go_to_cart(self):
        # Метод открывает корзину
        cart_link = self.driver.find_element(*self.CART_LINK)
        cart_link.click()
