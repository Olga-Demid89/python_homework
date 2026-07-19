from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_navigation():
    driver = webdriver.Chrome()
    driver.maximize_window()

    driver.get("https://httpbin.org")
    sleep(2)

    start_url = driver.current_url

    click_link = driver.find_element(By.LINK_TEXT, "HTML form")
    click_link.click()

    assert driver.current_url.endswith("/forms/post")
    f"Ожидался URL с окончанием /forms/post, но получен: {driver.current_url}"
    print("URL успешно изменился на /forms/post")

    driver.back()

    assert driver.current_url == start_url
    f"Ожидался исходный URL {start_url}, но получен: {driver.current_url}"
    print("Успешно вернулись на исходную страницу")

    driver.quit()
