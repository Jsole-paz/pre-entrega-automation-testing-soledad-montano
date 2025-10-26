import pytest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.helpers import login_saucedemo,get_driver
from selenium.webdriver.common.by import By

@pytest.fixture
def driver():

    driver = get_driver() #ejecuta la funcion get_driver de helpers.py
    yield driver #devuelve el driver para usar en los tests y mantiene la sesion abierta.
    driver.quit() #cierra la sesion despues de ejecutar el test.

def test_login(driver):
    login_saucedemo(driver)
    assert "/inventory.html" in driver.current_url

    titulo = driver.find_element(By.CSS_SELECTOR, 'div.header_secondary_container .title').text
    assert titulo == "Products"
    logo = driver.find_element (By.CLASS_NAME, 'app_logo').text
    assert logo == "Swag Labs"

def test_catalogo (driver):
    login_saucedemo(driver)

    products = driver.find_elements (By.CLASS_NAME, 'inventory_item')
    assert len(products) > 0
    driver.save_screenshot('./datos/imagenes/catalogo.png')

def test_carrito (driver):
    login_saucedemo(driver)

    products = driver.find_elements(By.CLASS_NAME, 'inventory_item')
    assert len(products) > 0

    products[0].find_element(By.TAG_NAME,'button').click()
    products[1].find_element(By.TAG_NAME,'button').click()
    products[2].find_element(By.TAG_NAME,'button').click()

    badge = driver.find_element(By.CLASS_NAME,'shopping_cart_badge').text
    assert badge == '3'
    driver.save_screenshot('./datos/imagenes/carrito.png')

def test_lista_de_compra (driver):
    login_saucedemo(driver)

    products = driver.find_elements(By.CLASS_NAME, 'inventory_item')
    for i in range (3):
        products[i].find_element(By.TAG_NAME,'button').click()

    driver.find_element(By.CLASS_NAME,'shopping_cart_link').click()
    assert '/cart.html' in driver.current_url

    carrito_elementos = driver.find_elements(By.CLASS_NAME,'inventory_item_name')
    assert len(carrito_elementos) == 3

    assert carrito_elementos[0].text == 'Sauce Labs Backpack'
    assert carrito_elementos[1].text == 'Sauce Labs Bike Light'
    assert carrito_elementos[2].text == 'Sauce Labs Bolt T-Shirt'

    driver.save_screenshot('./datos/imagenes/lista-de-compra.png')