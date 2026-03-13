import pytest
import allure
from allure import severity_level
from selenium import webdriver

from login_page import LoginPage
from inventory_page import InventoryPage
from cart_page import CartPage
from checkout_page import CheckoutPage


@allure.title("Проверка итоговой суммы в магазине (корзина)")
@allure.description(
    "Добавляем несколько товаров, заполняем форму оформления и проверяем итоговую сумму заказа."
)
@allure.feature("Shop")
@allure.severity(severity_level.CRITICAL)
@pytest.mark.shop
def test_shop_total():
    """
    Тест проверки корректности итоговой суммы заказа.
    """
    driver = webdriver.Firefox()
    driver.maximize_window()

    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)
    checkout_page = CheckoutPage(driver)

    try:
        with allure.step("Открыть страницу логина и выполнить вход"):
            login_page.open()
            login_page.login("standard_user", "secret_sauce")

        with allure.step("Добавить товары в корзину"):
            inventory_page.add_backpack()
            inventory_page.add_tshirt()
            inventory_page.add_onesie()

        with allure.step("Перейти в корзину и начать оформление"):
            inventory_page.go_to_cart()
            cart_page.click_checkout()

        with allure.step("Заполнить форму оплаты"):
            checkout_page.fill_form("Alex", "Ivanov", "12345")

        @allure.step("Проверка: итоговая строка равна '{expected}'")
        def check_total(actual: str, expected: str) -> None:
            """
            Шаг-проверка итоговой суммы.

            Параметры:
                actual (str): Текст суммы, полученный со страницы.
                expected (str): Ожидаемая строка суммы.

            Возвращает:
                None
            """
            assert actual == expected, f"Ожидали {expected}, получили {actual}"

        total = checkout_page.get_total()

        with allure.step("Проверить итоговую сумму заказа"):
            check_total(total, "Total: $58.29")

    finally:
        driver.quit()
