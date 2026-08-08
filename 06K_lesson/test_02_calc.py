from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_calc():
    driver = webdriver.Chrome()
    driver.maximize_window()
    wait = WebDriverWait(driver, 60)
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    time_wait = wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, "#delay")
        ))
    time_wait.clear()
    time_wait.send_keys("45")

    btn_7 = wait.until(EC.presence_of_element_located(
        (By.XPATH, "//*[@id='calculator']/div[2]/span[1]")))
    btn_7.click()

    btn_plus = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//*[@id='calculator']/div[2]/span[4]")
        ))
    btn_plus.click()

    btn_8 = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//*[@id='calculator']/div[2]/span[2]")
            ))
    btn_8.click()

    btn_equals = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//*[@id='calculator']/div[2]/span[15]")
            ))
    btn_equals.click()

    result_element = wait.until(EC.text_to_be_present_in_element(
        (By.CLASS_NAME, "screen"), "15"
        ))

    result_element = driver.find_element(By.CLASS_NAME, "screen")
    assert (
        result_element.text.strip() == "15"
        ), f"Ожидалось '15', но получено '{result_element.text}'"

    driver.quit()
