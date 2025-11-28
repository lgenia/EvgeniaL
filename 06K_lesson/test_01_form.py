from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


def test_buttons():
    driver = webdriver.Edge()
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    driver = WebDriverWait(7)

    first_name = driver.find_element(
        By.CSS_SELECTOR, "[name='first-name']")
    first_name.send_keys('Иван')
    first_name.click()

    last_name = driver.find_element(By.CSS_SELECTOR, "[name='last-name']")
    last_name.send_keys('Петров')
    last_name.click()

    address = driver.find_element(
        By.CSS_SELECTOR, "[name='address']")
    address.send_keys('Ленина, 55-3')
    address.click()

    mail = driver.find_element(
        By.CSS_SELECTOR, "[name='e-mail']")
    mail.send_keys("test@skypro.com")
    mail.click()

    phone = driver.find_element(
        By.CSS_SELECTOR, "[name='phone']")
    phone.send_keys("+7985899998787")
    phone.click()

    city = driver.find_element(
        By.CSS_SELECTOR, "[name='city']")
    city.send_keys("Москва")
    city.click()

    contry = driver.find_element(
        By.CSS_SELECTOR, "[name='country']")
    contry.send_keys("Россия")
    contry.click()

    job = driver.find_element(
        By.CSS_SELECTOR, "[name='job-position']")
    job.send_keys("QA")
    job.click()

    company = driver.find_element(
        By.CSS_SELECTOR, "[name='company']")
    company.send_keys("SkyPro")
    company.click()

    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    zip_code = driver.find_element(
            By.ID, "zip-code").value_of_css_property("background-color")
    assert zip_code == "rgba(248, 215, 218, 1)"

    fields = ["first-name", "last-name", "address", "e-mail", "phone",
              "city", "country", "job-position", "company"]
    for field in fields:
        tabs = driver.find_element(
            By.ID, field).value_of_css_property("background-color")
        assert tabs == "rgba(209, 231, 221, 1)"

    driver.quit()
