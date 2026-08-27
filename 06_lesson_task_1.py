from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Откройте страницу https://the-internet.herokuapp.com/dynamic_controls
def test_dynamic_controls():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)
    driver.maximize_window()
    driver.get("https://the-internet.herokuapp.com/dynamic_controls")


# Нажмите кнопку Remove.
    button_remove = wait.until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, "button[onclick='swapCheckbox()']")
    ))
    button_remove.click()

# Дождитесь появления текста It's gone!
    message_element = wait.until(EC.text_to_be_present_in_element(
        (By.ID, "message"), "It's gone!")
    )
    message_element = driver.find_element(By.ID, "message")
    assert message_element.text == "It's gone!", "Сообщение 'It's gone!' "
    "не появилось"

# Нажмите кнопку Enable.
    button_enable = wait.until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, "#input-example > button")
    ))
    button_enable.click()

# Дождитесь, когда поле ввода станет активным.
    input_field = wait.until(EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="input-example"]/input')
    ))
    assert input_field.is_enabled(), "Поле ввода не стало активным"

# Проверьте, что поле действительно стало активным.
    input_field.send_keys("Hello!")
    assert input_field.get_attribute("value") == "Hello!", "Текст не ввелся в "
    "поле"

    driver.quit()
