import os
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"

def create_driver():
    browser = os.getenv("BROWSER", "edge").lower()
    if browser == "edge":
        return webdriver.Edge()
    if browser == "safari":
        return webdriver.Safari()
    pytest.skip(f"Unsupported browser: {browser}. Use 'edge' or 'safari' via BROWSER env var.")


def fill_input(wait, name, value):
    el = wait.until(EC.element_to_be_clickable((By.NAME, name)))
    el.clear()
    if value:
        el.send_keys(value)


def test_form_highlights():
    driver = create_driver()
    wait = WebDriverWait(driver, 10)
    try:
        driver.get(URL)

        data = {
            "first-name": "Иван",
            "last-name": "Петров",
            "address": "Ленина, 55-3",
            "e-mail": "test@skypro.com",
            "phone": "+7985899998787",
            "zip-code": "",
            "city": "Москва",
            "country": "Россия",
            "job-position": "QA",
            "company": "SkyPro",
        }

       
        for name, value in data.items():
            if name == "zip-code":
                continue
            fill_input(wait, name, value)

        submit_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']")))
        submit_btn.click()

        wait.until(EC.presence_of_element_located((By.ID, "first-name")))

        ids = ["first-name", "last-name", "address", "zip-code", "city", "country", "e-mail", "phone", "job-position", "company"]

        zip_el = wait.until(EC.presence_of_element_located((By.ID, "zip-code")))
        zip_classes = zip_el.get_attribute("class") or ""
        assert "alert-danger" in zip_classes, f"Ожидалось, что поле Zip code подсвечено красным, классы: {zip_classes}"
        
        for id_ in ids:
            if id_ == "zip-code":
                continue
            el = wait.until(EC.presence_of_element_located((By.ID, id_)))
            classes = el.get_attribute("class") or ""
            assert "alert-success" in classes, f"Ожидалось, что поле {id_} подсвечено зелёным, классы: {classes}"

    finally:
        driver.quit()