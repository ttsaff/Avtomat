from selenium import webdriver
import pytest

from login_page import LoginPage
from inventory_page import InventoryPage
from cart_page import CartPage
from checkout_page import CheckoutPage

@pytest.mark.shop
def test_shop_total():

    driver = webdriver.Firefox()
    driver.maximize_window()

    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)
    checkout_page = CheckoutPage(driver)

    try:
        login_page.open()

        login_page.login("standard_user", "secret_sauce")

        inventory_page.add_backpack()
        inventory_page.add_tshirt()
        inventory_page.add_onesie()

        inventory_page.go_to_cart()

        cart_page.click_checkout()

        checkout_page.fill_form(
            "Alex",
            "Ivanov",
            "12345"
        )

        total = checkout_page.get_total()

        assert total == "Total: $58.29"

    finally:
        driver.quit()