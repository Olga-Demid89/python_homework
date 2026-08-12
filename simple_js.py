from selenium import webdriver


driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://ru.wikipedia.org/wiki/")


title = driver.execute_script("return document.title;")
url = driver.execute_script("return window.location.href;")


print(f"Заголовок: {title}")
print(f"URL: {url}")

driver.quit()
