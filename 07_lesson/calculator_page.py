from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 60)
        self.url = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"

        self._delay_input = (By.CSS_SELECTOR, "#delay")
        self._btn_7 = (By.XPATH, "//*[@id='calculator']/div[2]/span[1]")
        self._btn_plus = (By.XPATH, "//*[@id='calculator']/div[2]/span[4]")
        self._btn_8 = (By.XPATH, "//*[@id='calculator']/div[2]/span[2]")
        self._btn_equals = (By.XPATH, "//*[@id='calculator']/div[2]/span[15]")
        self._screen = (By.CLASS_NAME, "screen")

    def open(self):
        self.driver.get(self.url)

    def set_delay(self, seconds: str):
        delay_field = self.wait.until(EC.presence_of_element_located
        (self._delay_input)
        )
        delay_field.clear()
        delay_field.send_keys(seconds)

    def click_7(self):
        self.wait.until(EC.element_to_be_clickable(self._btn_7)).click()

    def click_plus(self):
        self.wait.until(EC.element_to_be_clickable(self._btn_plus)).click()

    def click_8(self):
        self.wait.until(EC.element_to_be_clickable(self._btn_8)).click()

    def click_equals(self):
        self.wait.until(EC.element_to_be_clickable(self._btn_equals)).click()

    def get_result(self) -> str:
        self.wait.until(EC.text_to_be_present_in_element
        (self._screen, "15")
        )
        return self.driver.find_element(*self._screen).text.strip()
