import pytest
from page.login_page import LoginPage
from page.inventory_page import InventoryPage
from page.cart_page import CartPage
from page.checkout_page import CheckoutPage
from page.checkout_complete_page import CheckoutCompletePage
import time

def test_complete_purchase_flow(driver):
    login = LoginPage(driver)
    inventory = InventoryPage(driver)
    cart = CartPage(driver)
    checkout = CheckoutPage(driver)
    complete = CheckoutCompletePage(driver)

    login.open()
    login.login("standard_user","secret_sauce")
    time.sleep(5)

    inventory.add_product_to_card(0)
    inventory.got_to_card()

    cart.go_to_checkout()

    checkout.fill_customer_info("Jane", "Smith", "54321")
    checkout.continue_to_overview()

    driver.get("https://www.saucedemo.com/checkout-complete.html")

    assert complete.is_at_page()
    assert "Thank you for your order!" in complete.get_success_message()
    assert complete.is_pony_express_image_displayed()

    complete.back_to_home()
    assert inventory.is_at_page()