from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class CheckoutPage:
    """
    Страница оформления заказа (Checkout).

    Атрибуты:
        driver (WebDriver): Экземпляр WebDriver для управления браузером.
    """

    def __init__(self, driver: WebDriver) -> None:
        """
        Инициализация страницы оформления заказа.

        Параметры:
            driver (WebDriver): WebDriver для управления браузером.

        Возвращает:
            None
        """
        self.driver = driver

    first_name = (By.ID, "first-name")
    last_name = (By.ID, "last-name")
    postal_code = (By.ID, "postal-code")
    continue_button = (By.ID, "continue")
    total_price = (By.CLASS_NAME, "summary_total_label")

    def enter_first_name(self, name: str) -> None:
        """
        Вводит имя покупателя в форму.

        Параметры:
            name (str): Имя покупателя.

        Возвращает:
            None
        """
        self.driver.find_element(*self.first_name).send_keys(name)

    def enter_last_name(self, name: str) -> None:
        """
        Вводит фамилию покупателя в форму.

        Параметры:
            name (str): Фамилия покупателя.

        Возвращает:
            None
        """
        self.driver.find_element(*self.last_name).send_keys(name)

    def enter_postal_code(self, code: str) -> None:
        """
        Вводит почтовый индекс (ZIP) в форму.

        Параметры:
            code (str): Почтовый индекс/ZIP-код.

        Возвращает:
            None
        """
        self.driver.find_element(*self.postal_code).send_keys(code)

    def click_continue(self) -> None:
        """
        Нажимает кнопку "Continue" (продолжить оформление).

        Параметры:
            отсутствуют (кроме self)

        Возвращает:
            None
        """
        self.driver.find_element(*self.continue_button).click()

    def fill_form(self, first: str, last: str, zip_code: str) -> None:
        """
        Заполняет поля формы и нажимает продолжить.

        Параметры:
            first (str): Имя покупателя.
            last (str): Фамилия покупателя.
            zip_code (str): Почтовый индекс/ZIP-код.

        Возвращает:
            None
        """
        self.enter_first_name(first)
        self.enter_last_name(last)
        self.enter_postal_code(zip_code)
        self.click_continue()

    def get_total(self) -> str:
        """
        Получает текст общей суммы заказа, как отображается на странице.

        Параметры:
            отсутствуют (кроме self)

        Возвращает:
            str: Текст общей суммы, например "Total: $58.29".
        """
        return self.driver.find_element(*self.total_price).text
