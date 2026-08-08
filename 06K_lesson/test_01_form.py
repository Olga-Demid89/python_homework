from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_form():
    driver = webdriver.Edge()
    driver.maximize_window()
    wait = WebDriverWait(driver, 10)
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    input_first_name = wait.until(EC.presence_of_element_located(
        (By.NAME, "first-name")
        ))
    input_first_name.send_keys("Иван")

    input_last_name = wait.until(EC.presence_of_element_located(
        (By.NAME, "last-name")
        ))
    input_last_name.send_keys("Петров")

    input_address = wait.until(EC.presence_of_element_located(
        (By.NAME, "address")
        ))
    input_address.send_keys("Ленина, 55-3")

    input_email = wait.until(EC.presence_of_element_located(
        (By.NAME, "e-mail")
        ))
    input_email.send_keys("test@skypro.com")

    input_phone = wait.until(EC.presence_of_element_located(
        (By.NAME, "phone")
        ))
    input_phone.send_keys("+7985899998787")

    zip_code = wait.until(EC.presence_of_element_located(
        (By.NAME, "zip-code")
        ))
    zip_code.clear()

    input_city = wait.until(EC.presence_of_element_located(
        (By.NAME, "city")
        ))
    input_city.send_keys("Москва")

    input_country = wait.until(EC.presence_of_element_located(
        (By.NAME, "country")
        ))
    input_country.send_keys("Россия")

    input_job_position = wait.until(EC.presence_of_element_located(
        (By.NAME, "job-position")
        ))
    input_job_position.send_keys("QA")

    input_company = wait.until(EC.presence_of_element_located(
        (By.NAME, "company")
        ))
    input_company.send_keys("SkyPro")

    btn_submit = wait.until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, "button[type='submit']")
        ))
    btn_submit.click()

    wait.until(EC.visibility_of_element_located((By.ID, "zip-code")))

    zip_class = driver.find_element(By.ID, "zip-code").get_attribute("class")
    assert (
        "alert-danger" in zip_class
        ), "Поле Zip code должно быть подсвечено красным!"

    success_fields = [
        "first-name", "last-name", "address", "e-mail",
        "phone", "city", "country", "job-position", "company"
    ]

    for field_id in success_fields:
        field_class = driver.find_element(
            By.ID, field_id).get_attribute("class")
        assert (
            "alert-success" in field_class
            ), f"Поле {field_id} должно быть подсвечено зеленым!"

    driver.quit()
