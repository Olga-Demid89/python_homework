from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_form_submission():
    driver = webdriver.Chrome()
    driver.get("https://httpbin.org/forms/post")
    sleep(3)

    start_url = driver.current_url

    name_field = driver.find_element(By.NAME, "custname")
    name_field.send_keys("Ольга")

    submit_btn = driver.find_element(By.XPATH,
                                     "//button[text()='Submit order']")
    submit_btn.click()

    assert driver.current_url != start_url
    f"Ожидался исходный URL {start_url}, но получен: {driver.current_url}"
    print("URL изменился")

    driver.quit()
