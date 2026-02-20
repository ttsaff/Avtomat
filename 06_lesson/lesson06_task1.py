from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

try:
    driver.get("http://uitestingplayground.com/ajax")

    wait = WebDriverWait(driver, 15)

    button = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn-primary"))
    )
    button.click()

    success_label = wait.until(
        EC.visibility_of_element_located((By.CLASS_NAME, "bg-success"))
    )

    result_text = success_label.text

    print(result_text)

finally:
    driver.quit()