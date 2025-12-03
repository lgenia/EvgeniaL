import pytest
from selenium import webdriver


@pytest.fixture(scope="module")
def browser():
    # Инициализация и закрытие браузера
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_calculator_with_page_object(browser):
    calculator_page = CalculatorPage(browser)

    # Открываем страницу калькулятора
    calculator_page.open()

    # Устанавливаем задержку на 45 секунд
    calculator_page.set_delay("45")

    # Кликаем последовательно на кнопки: 7, +, 8, =
    calculator_page.click_button("7")
    calculator_page.click_button("+")
    calculator_page.click_button("8")
    calculator_page.click_button("=")

    # Ждём появления результата
    result_element = calculator_page.wait_for_result(timeout=46)

    # Получаем вывод результата и проверяем
    actual_result = calculator_page.get_screen_value()
    assert actual_result == "15", f"Expected result is '15', but got '{actual_result}'"