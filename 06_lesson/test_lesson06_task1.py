from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_dynamic_loading():
    driver = webdriver.Chrome()
    driver.maximize_window()
    wait = WebDriverWait(driver, 10)
    driver.get("https://the-internet.herokuapp.com/dynamic_loading/2")

    start_btn = wait.until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, "#start button")
    ))
    start_btn.click()

    mеssage_element = wait.until(EC.visibility_of_element_located(
        (By.ID, "finish")
    ))

    driver.save_screenshot("screenshots/message.png")

    assert mеssage_element.text == "Hello World!", "Сообщение 'Hello World! не"
    "появилось"

    driver.quit()
