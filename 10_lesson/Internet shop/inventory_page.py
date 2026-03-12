from typing import Any
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class InventoryPage:
    """
    Страница каталога товаров (Inventory).

    Атрибуты:
        driver (WebDriver): Экземпляр WebDriver для управления браузером.
    """

    def __init__(self, driver: WebDriver) -> None:
        """
        Инициализация страницы каталога товаров.

        Параметры:
            driver (WebDriver): WebDriver для управления браузером.

        Возвращает:
            None
        """
        self.driver = driver

    cart_button = (By.CLASS_NAME, "shopping_cart_link")

    def add_backpack(self) -> None:
        """
        Добавляет в корзину товар "sauce-labs-backpack".

        Параметры:
            отсутствуют (кроме self)

        Возвращает:
            None
        """
        self.driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()

    def add_tshirt(self) -> None:
        """
        Добавляет в корзину товар "sauce-labs-bolt-t-shirt".

        Параметры:
            отсутствуют (кроме self)

        Возвращает:
            None
        """
        self.driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()

    def add_onesie(self) -> None:
        """
        Добавляет в корзину товар "sauce-labs-onesie".

        Параметры:
            отсутствуют (кроме self)

        Возвращает:
            None
        """
        self.driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()

    def go_to_cart(self) -> None:
        """
        Переходит в корзину (клик по иконке корзины).

        Параметры:
            отсутствуют (кроме self)

        Возвращает:
            None
        """
        self.driver.find_element(*self.cart_button).click()