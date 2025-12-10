from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class InventoryPage:
    URL_CURRENT = "/inventory.html"
    MENU_BUTTON = (By.ID, 'react-burger-menu-btn')
    LINK_BUTTON = (By.ID, 'logout_sidebar_link')
    ADD_TO_CARD_BUTTON = (By.XPATH, "add-to-cart-sauce-labs-backpack")
    CARD_LINK = (By.CLASS_NAME, 'shopping_cart_link')

    def __init__(self, driver):
        self.driver = driver

    def is_at_page(self):
        return self.URL_CURRENT in self.driver.current_url
    
    def add_product_to_card(self,product_index=0):
        add_buttons = self.driver.find_elements(self.ADD_TO_CARD_BUTTON)
        if add_buttons and product_index < len(add_buttons):
            add_buttons[product_index].click()

    def got_to_card(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.CARD_LINK)
        ).click()

    def logout(self):
        self.driver.find_element(self.MENU_BUTTON).click()
        time.sleep(5)
        WebDriverWait(self.driver,10).until(
            EC.element_to_be_clickable(self.LINK_BUTTON)
        ).click()