from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def hacer_login(self, usuario, password):
        self.driver.find_element(By.ID, "user-name").send_keys(usuario)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.ID, "login-button").click()