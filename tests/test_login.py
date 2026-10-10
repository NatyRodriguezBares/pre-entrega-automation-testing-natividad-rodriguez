import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC




from pages.LoginPage import LoginPage



# import time #MALA PRACTICA....


@pytest.fixture(scope='module')
def driver():
    service = Service(ChromeDriverManager().install())
    options = Options()

    options.add_argument('--lang=es')
    driver = webdriver.Chrome(service=service, options=options)


    driver.implicitly_wait(10)

    yield driver 

    driver.quit()



def test_01_login(driver):

    # CREAR UN OBJETO
    login = LoginPage(driver)

    # login.ingresar_password()

    driver.get("https://www.saucedemo.com/")


    # login.ingresar_Usuario('standard_user')
    # login.ingresar_password('12345')

    login.hacer_login("standard_user","secret_sauce")


    # driver.find_element(By.ID, "user-name").send_keys("standard_user")
    # driver.find_element(By.ID, "password").send_keys("secret_sauce")
    # driver.find_element(By.ID, "login-button").click()

    assert "/inventory.html" in driver.current_url , "ERROR: No se redirigió a /inventory.html"