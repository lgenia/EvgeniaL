from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
    
    # Локаторы элементов
    USERNAME_FIELD = (By.ID, 'user-name')
    PASSWORD_FIELD = (By.ID, 'password')
    LOGIN_BUTTON = (By.ID, 'login-button')

    def enter_username(self, username):
        # Метод для ввода логина
        element = self.driver.find_element(*self.USERNAME_FIELD)
        element.send_keys(username)
    
    def enter_password(self, password):
        # Метод для ввода пароля
        element = self.driver.find_element(*self.PASSWORD_FIELD)
        element.send_keys(password)
    
    def click_login_button(self):
        # Метод для клика по кнопке входа
        button = self.driver.find_element(*self.LOGIN_BUTTON)
        button.click()
