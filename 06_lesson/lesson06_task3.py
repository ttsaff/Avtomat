from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome()

try:
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

    wait = WebDriverWait(driver, 20)

    wait.until(lambda d: len(d.find_elements(By.TAG_NAME, "img")) >= 4)

    images = driver.find_elements(By.TAG_NAME, "img")

    third_image = images[2]

    src_value = third_image.get_attribute("src")

    print(src_value)

finally:
    driver.quit()