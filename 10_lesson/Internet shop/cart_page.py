from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class CartPage:
    """
    Страница корзины.

    Атрибуты:
        driver (WebDriver): Экземпляр WebDriver для управления браузером.
    """

    def __init__(self, driver: WebDriver) -> None:
        """
        Инициализация страницы корзины.

        Параметры:
            driver (WebDriver): WebDriver для управления браузером.

        Возвращает:
            None
        """
        self.driver = driver

    checkout_button = (By.ID, "checkout")

    def click_checkout(self) -> None:
        """
        Нажимает кнопку "Checkout" (перейти к оформлению).

        Параметры:
            отсутствуют (кроме self)

        Возвращает:
            None
        """
        self.driver.find_element(*self.checkout_button).click()
