from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("http://uitestingplayground.com/classattr")

blue_button = driver.find_element(By.CLASS_NAME, "btn-primary")
blue_button.click()

time.sleep(4)
driver.quit()