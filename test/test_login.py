import pytest
from page.login_page import LoginPage
from datos.datos_login import casos_login
from utils.faker import get_login_faker

@pytest.mark.parametrize("username,password,login_bool",casos_login)
def test_login(driver, username, password, login_bool):
    loginPage = LoginPage(driver)
    loginPage.open()
    loginPage.login(username, password)

    if login_bool:
        assert "/inventory.html" in driver.current_url
    else:
        assert"/inventory.html" not in driver.current_url