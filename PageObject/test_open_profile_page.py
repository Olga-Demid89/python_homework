import faker
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def open_profile_page(driver):
    driver.get("https://gitflic.ru/user/olga89demid")
    driver.save_screenshot("screenshots/full_page.png")


def update_profile(driver, wait, new_user_name, new_last_name):
    edit_button = wait.until(EC.presence_of_element_located(
        (By.CLASS_NAME, "user-profile__edit")
    ))
    edit_button.click()
    username_input = wait.until(EC.presence_of_element_located(
        (By.ID, "name")
    ))
    username_input.clear()
    username_input.send_keys(new_user_name)

    surname_input = driver.find_element(By.ID, "surname")
    surname_input.clear()
    surname_input.send_keys(new_last_name)

    save_button = wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, ".gf-button.--success")
    ))
    save_button.click()


def get_user_name(wait):
    user_name = wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, "h6.mb-0")
    ))
    user_name.screenshot("screenshots/user_name.png")
    return user_name.text


def test_update_user_name(driver):
    wait = WebDriverWait(driver, 10)
    # Перейти на страницу профиля
    open_profile_page(driver)

    # Нажать кнопку редактирования профиля
    # Изменить Ф и И в форме
    # Сохранить изменения
    user_name = faker.Faker().first_name()
    last_name = faker.Faker().last_name()
    update_profile(driver, wait, user_name, last_name)

    # Вернуться на страницу профиля
    open_profile_page(driver)


    # Ожидаемый результат: Ф и И успешно изменены и отображается на странице
    # профиля
    assert get_user_name(wait) == user_name + " " + last_name