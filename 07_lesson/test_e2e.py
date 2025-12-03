import pytest
from selenium import webdriver
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.cart_page import CartPage
from pages.checkout_step_one_page import CheckoutStepOnePage
from pages.checkout_complete_page import CheckoutCompletePage

# Фикстура браузера
@pytest.fixture(scope="module")
def browser():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()

# Основной тест
def test_shopping_flow(browser):
    # Открываем сайт
    browser.get('https://www.saucedemo.com/')

    # Страница авторизации
    login_page = LoginPage(browser)
    login_page.enter_username('standard_user')
    login_page.enter_password('secret_sauce')
    login_page.click_login_button()

    # Главная страница магазина
    main_page = MainPage(browser)
    main_page.add_items_to_cart('Sauce Labs Backpack', 'Sauce Labs Bolt T-Shirt', 'Sauce Labs Onesie')
    main_page.go_to_cart()

    # Корзина
    cart_page = CartPage(browser)
    cart_page.checkout()

    # Оформляем заказ
    checkout_step_one_page = CheckoutStepOnePage(browser)
    checkout_step_one_page.fill_personal_data('Иван', 'Петров', '123456')
    checkout_step_one_page.continue_checkout()

    # Получение итоговой суммы
    complete_page = CheckoutCompletePage(browser)
    total_amount = complete_page.get_total_price()

    # Проверяем итоговую сумму
    assert total_amount == 'Total: $58.29'
