import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="session")
def driver():
    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://gitflic.ru/")
    driver.add_cookie({
        "name": "SESSION",
        "value": "MjRmNjRkMDItNmZjOC00ZTU3LWJiYmYtMGFjMTM1OTA4MzI0",
        "domain": "gitflic.ru"
    })
    driver.add_cookie({
            "name": "cookiesAccepted",
            "value": "true",
            "domain": "gitflic.ru"
    })
    driver.refresh()
    yield driver
    driver.quit()
