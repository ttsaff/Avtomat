from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = Options()
options.add_argument("--start-maximized")

driver = webdriver.Chrome(options=options)

try:
    driver.get("http://uitestingplayground.com/dynamicid")

    wait = WebDriverWait(driver, 10)
    blue_button = wait.until(
        EC.element_to_be_clickable((By.CLASS_NAME, "btn-primary"))
    )

    blue_button.click()

finally:
    driver.quit()