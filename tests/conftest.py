import os
from datetime import datetime

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

from pages.LoginPage import LoginPage
from utils.logger import logger

@pytest.fixture
def driver():
    service = Service(ChromeDriverManager().install())
    options = Options()
    options.add_argument('--lang=es')

    driver = webdriver.Chrome(service=service, options=options)
    driver.implicitly_wait(10)

    driver.get("https://www.saucedemo.com/")

    login = LoginPage(driver)
    login.hacer_login("standard_user", "secret_sauce")

    yield driver

    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call":
        if report.passed:
            logger.info("PRUEBA APROBADA: %s", item.name)
        elif report.failed:
            logger.error("PRUEBA FALLIDA: %s", item.name)

    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver")

        if driver:
            os.makedirs("reports/capturas", exist_ok=True)
            fecha = datetime.now().strftime("%Y%m%d_%H%M%S")
            archivo = f"reports/capturas/error_{item.name}_{fecha}.png"

            driver.save_screenshot(archivo)
            print(f"\nCaptura guardada en: {archivo}")