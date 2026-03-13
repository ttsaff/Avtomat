from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class CalculatorPage:
    """
    Страница "Slow Calculator".

    Атрибуты:
        driver (WebDriver): Экземпляр WebDriver для управления браузером.
        url (str): URL страницы калькулятора.
    """

    def __init__(self, driver: WebDriver) -> None:
        """
        Инициализация страницы калькулятора.

        Параметры:
            driver (WebDriver): WebDriver для управления браузером.

        Возвращает:
            None
        """
        self.driver = driver
        self.url = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"

    delay_input = (By.CSS_SELECTOR, "#delay")
    result = (By.CSS_SELECTOR, ".screen")

    def open(self) -> None:
        """
        Открывает страницу калькулятора.

        Параметры:
            отсутствуют (кроме self)

        Возвращает:
            None
        """
        self.driver.get(self.url)

    def set_delay(self, value: str) -> None:
        """
        Устанавливает задержку выполнения операций калькулятора.

        Параметры:
            value (str): Значение задержки (в миллисекундах или как
            предусмотрено страницей) в виде строки.

        Возвращает:
            None
        """
        field = self.driver.find_element(*self.delay_input)
        field.clear()
        field.send_keys(value)

    def click_button(self, value: str) -> None:
        """
        Нажимает кнопку калькулятора по видимому тексту.

        Параметры:
            value (str): Текст на кнопке (например, "7", "+", "=" и т.д.).

        Возвращает:
            None
        """
        button = self.driver.find_element(By.XPATH, f"//span[text()='{value}']")
        button.click()

    def get_result(self) -> str:
        """
        Возвращает отображаемый результат на экране калькулятора.

        Параметры:
            отсутствуют (кроме self)

        Возвращает:
            str: Текст результата (строка).
        """
        return self.driver.find_element(*self.result).text
