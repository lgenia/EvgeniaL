from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Firefox()
driver.get("http://the-internet.herokuapp.com/login")
input_login = driver.find_element(By.ID, "username")
input_login.send_keys("tomsmith")
input_pass = driver.find_element(By.ID, 'password')
input_pass.send_keys("SuperSecretPassword!")
button = driver.find_element(By.CLASS_NAME, "radius")
button.click()


sleep(5)
msg = driver.find_element(By.ID, "flash")


print(msg.text)

driver.quit()
