import pytest
from page.login_page import LoginPage
from page.inventory_page import InventoryPage
from page.cart_page import CartPage
from page.checkout_page import CheckoutPage
import time

def test_checkout_process(driver):
    login = LoginPage(driver)
    inventory = InventoryPage(driver)
    cart = CartPage(driver)
    checkout = CheckoutPage(driver)

    login.open()
    login.login("standard_user","secret_sauce")
    time.sleep(5)

    inventory.add_product_to_card(0)
    inventory.go_to_cart()
    time.sleep(5)
    cart.go_to_checkout()
    time.sleep(5)

    assert checkout.is_ar_page()

    checkout.fill_customer_info("John", "Doe", "12345")
    checkout.continue_to_overview()

    assert "checkout-step-two" in driver.current_url

def test_checkout_validation(driver):
    login = LoginPage(driver)
    inventory = InventoryPage(driver)
    cart = CartPage(driver)
    checkout = CheckoutPage(driver)

    login.open()
    login.login("standard_user","secret_sauce")
    time.sleep(5)

    inventory.add_product_to_card(0)
    inventory.got_to_card()
    cart.go_to_checkout()

    checkout.continue_to_overview()

    error_massage = checkout.get_error_message()
    assert "First Name is required" in error_massage