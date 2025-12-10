import pytest
from page.login_page import LoginPage
from page.inventory_page import InventoryPage
from page.cart_page import CartPage
import time

def test_cart_operations(driver):
    login = LoginPage(driver)
    inventory = InventoryPage(driver)
    cart = CartPage(driver)

    login.open()
    login.login("standard_user","secret_sauce")
    time.sleep(5)

    inventory.add_product_to_card(0)
    inventory.got_to_card()
    time.sleep(5)

    assert cart.is_at_page()
    assert cart.get_cart_items_count() == 2

    cart.continue_shopping()
    time.sleep(5)
    assert inventory.is_at_page()

def test_remove_from_cart(driver):
    login = LoginPage(driver)
    inventory = InventoryPage(driver)
    cart = CartPage(driver)

    login.open()
    login.login("standard_user","secret_sauce")
    time.sleep(5)

    inventory.add_product_to_card(0)
    inventory.got_to_card()
    time.sleep(5)

    initial_count = cart.get_cart_items_count()
    cart.remove_item(0)
    time.sleep(5)

    assert cart.get_cart_items_count() == initial_count - 1