import pytest
import os
import sys
from page.login_page import LoginPage
from page.inventory_page import InventoryPage
from page.cart_page import CartPage
import time

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def test_cart_operations(driver):
    login = LoginPage(driver)
    inventory = InventoryPage(driver)
    cart = CartPage(driver)

    login.open()
    login.login("standard_user","secret_sauce")
    time.sleep(5)

    inventory.add_product_to_card(0)
    inventory.get_to_card()
    time.sleep(5)

    assert cart.is_at_page()
    assert cart.get_cart_items_count() == 1
    driver.save_screenshot('./imagenes-test/cart_operations.png')

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
    inventory.get_to_card()
    time.sleep(5)

    initial_count = cart.get_cart_items_count()
    cart.remove_item(0)
    time.sleep(5)
    driver.save_screenshot('./imagenes-test/remove_from_cart.png')
    assert cart.get_cart_items_count() == initial_count - 1