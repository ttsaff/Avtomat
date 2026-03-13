import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from calculator_page import CalculatorPage


@pytest.mark.calculator
def test_slow_calculator():

    driver = webdriver.Chrome()
    driver.maximize_window()

    page = CalculatorPage(driver)

    try:
        page.open()

        page.set_delay("45")

        page.click_button("7")
        page.click_button("+")
        page.click_button("8")
        page.click_button("=")

        wait = WebDriverWait(driver, 50)

        wait.until(lambda d: page.get_result() == "15")

        assert page.get_result() == "15"

    finally:
        driver.quit()