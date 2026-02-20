from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

try:
    driver.get("http://uitestingplayground.com/textinput")

    wait = WebDriverWait(driver, 10)

    input_field = wait.until(
        EC.presence_of_element_located((By.ID, "newButtonName"))
    )
    input_field.send_keys("SkyPro")

    button = driver.find_element(By.ID, "updatingButton")
    button.click()

    updated_text = button.text

    print(updated_text)

finally:
    driver.quit()