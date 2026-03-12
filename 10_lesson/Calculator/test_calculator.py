import pytest
import allure
from allure import severity_level
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

from calculator_page import CalculatorPage


@allure.title("Проверка работы Slow Calculator: 7 + 8 = 15")
@allure.description("Открываем slow-calculator, настраиваем задержку, вводим 7 + 8 и проверяем результат 15.")
@allure.feature("Calculator")
@allure.severity(severity_level.NORMAL)
@pytest.mark.calculator
def test_slow_calculator():
    """
    Тест для замедленного калькулятора.
    """
    driver = webdriver.Chrome()
    driver.maximize_window()

    page = CalculatorPage(driver)

    try:
        with allure.step("Открыть страницу калькулятора"):
            page.open()

        with allure.step("Установить задержку выполнения операций"):
            page.set_delay("5")

        with allure.step("Ввести выражение 7 + 8 и выполнить"):
            page.click_button("7")
            page.click_button("+")
            page.click_button("8")
            page.click_button("=")

        wait = WebDriverWait(driver, 50)

        with allure.step("Ожидание результата '15'"):
            wait.until(lambda d: page.get_result() == "15")

        @allure.step("Проверка: результат равен '{expected}'")
        def check_result(actual: str, expected: str) -> None:
            """
            Шаг-проверка результата.

            Параметры:
                actual (str): Фактический результат, полученный со страницы.
                expected (str): Ожидаемый результат.

            Возвращает:
                None
            """
            assert actual == expected, f"Ожидали {expected}, получили {actual}"

        check_result(page.get_result(), "15")

    finally:
        driver.quit()