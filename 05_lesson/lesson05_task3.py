from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Firefox()
driver.get("http://the-internet.herokuapp.com/inputs")
input = driver.find_element(By.TAG_NAME, "input")
input.send_keys('Sky')


sleep(2)
input.clear()


sleep(2)
input.send_keys('Pro')

sleep(2)
driver.quit()
