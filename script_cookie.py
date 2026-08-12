from time import sleep
from selenium import webdriver


driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://gitflic.ru/")


driver.add_cookie({
    "name": "SESSION",
    "value": "N2QxNDk0NzYtMzJmOC00MmM2LTg3MTItNjc1ZTBhYzhkNWNk",
    "domain": "gitflic.ru"
})

driver.add_cookie({
    "name": "cookiesAccepted",
    "value": "true",
    "domain": "gitflic.ru"
})

driver.refresh()

driver.get("https://gitflic.ru/user/olga89demid")

sleep(3)

driver.delete_all_cookies()
driver.refresh()
sleep(5)

driver.quit()
