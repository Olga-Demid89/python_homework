from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_session_storage_auth():
    driver = webdriver.Chrome()
    driver.maximize_window()
    wait = WebDriverWait(driver, 10)
    driver.get("https://gitflic.ru/")

    driver.add_cookie({
        "name": "SESSION",
        "value": "YzhkMmI0MzMtMWZhMC00MDU2LThiMTctNWU1N2IwMzk4NTFk",
        "domain": "gitflic.ru"
    })

    driver.refresh()
    wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))

    driver.get("https://gitflic.ru/user/olga89demid")

    url1 = driver.current_url
    print("URL Пользователя 1:", url1)

    driver.delete_cookie("SESSION")

    driver.add_cookie({
        "name": "SESSION",
        "value": "MDdmYmE4ODYtOTE5Ni00NjQzLWJiZDUtYTVkN2U1ZWE1OWY1",
        "domain": "gitflic.ru"
    })

    driver.refresh()
    wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))

    driver.get("https://gitflic.ru/user/olga_1989")

    url2 = driver.current_url
    print("URL Пользователя 2:", url2)

    assert url1 != url2, f"URL должны различаться: url1={url1}, url2={url2}"
    print("URL различаются — проверка пройдена")

    driver.quit()
