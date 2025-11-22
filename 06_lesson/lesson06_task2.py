from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(
    service=ChromeService(
        ChromeDriverManager().install()))
driver.implicitly_wait(50)
driver.get("http://uitestingplayground.com/textinput")
pole_voda = driver.find_element(
    By.CSS_SELECTOR, "#newButtonName").send_keys("SkyPro")
button = driver.find_element(By.CSS_SELECTOR, "#updatingButton").click()
button_text = driver.find_element(By.CSS_SELECTOR, '#updatingButton')


text = button_text.text


print(text)
