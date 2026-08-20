from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.url = "https://www.saucedemo.com/"

        self._username_input = (By.ID, "user-name")
        self._password_input = (By.ID, "password")
        self._login_button = (By.ID, "login-button")

    def open(self):
        self.driver.get(self.url)

    def login(self, username, password):
        self.wait.until(EC.visibility_of_element_located
        (self._username_input)
        ).send_keys(username)
        self.driver.find_element(*self._password_input).send_keys(password)
        self.driver.find_element(*self._login_button).click()


class MainPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

        self._backpack_btn = (By.ID, "add-to-cart-sauce-labs-backpack")
        self._bolt_tshirt_btn = (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
        self._onesie_btn = (By.ID, "add-to-cart-sauce-labs-onesie")
        self._cart_link = (By.CLASS_NAME, "shopping_cart_link")

    def add_backpack(self):
        self.wait.until(EC.element_to_be_clickable
        (self._backpack_btn)
        ).click()

    def add_bolt_tshirt(self):
        self.driver.find_element(*self._bolt_tshirt_btn).click()

    def add_onesie(self):
        self.driver.find_element(*self._onesie_btn).click()

    def go_to_cart(self):
        self.driver.find_element(*self._cart_link).click()


class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

        self._checkout_button = (By.ID, "checkout")

    def click_checkout(self):
        self.wait.until(EC.element_to_be_clickable
        (self._checkout_button)
        ).click()


class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

        self._first_name_input = (By.ID, "first-name")
        self._last_name_input = (By.ID, "last-name")
        self._postal_code_input = (By.ID, "postal-code")
        self._continue_button = (By.ID, "continue")
        self._total_label = (By.CLASS_NAME, "summary_total_label")

    def fill_checkout_form(self, first_name, last_name, postal_code):
        self.wait.until(EC.visibility_of_element_located
        (self._first_name_input)
        ).send_keys(first_name)
        self.driver.find_element(*self._last_name_input).send_keys(last_name)
        self.driver.find_element(*self._postal_code_input).send_keys(postal_code)
        self.driver.find_element(*self._continue_button).click()

    def get_total_price(self) -> str:
        total_element = self.wait.until(EC.visibility_of_element_located
        (self._total_label)
        )
        return total_element.text
