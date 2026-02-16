from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = Options()
options.add_argument("--width=1200")
options.add_argument("--height=800")

driver = webdriver.Firefox(options=options)

try:
    driver.get("http://the-internet.herokuapp.com/inputs")

    wait = WebDriverWait(driver, 10)
    input_field = wait.until(
        EC.presence_of_element_located((By.TAG_NAME, "input"))
    )

    input_field.send_keys("Sky")

    input_field.clear()

    input_field.send_keys("Pro")

finally:
    driver.quit()