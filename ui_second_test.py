from selenium import webdriver
from selenium.webdriver.common.by import By


def test_image_loading():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(20)
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

    compass_img = driver.find_element(By.ID, "compass")
    calendar_img = driver.find_element(By.ID, "calendar")
    award_img = driver.find_element(By.ID, "award")
    landscape_img = driver.find_element(By.ID, "landscape")

    images = [compass_img, calendar_img, award_img, landscape_img]
    expected_files = [
        "compass.png",
        "calendar.png",
        "award.png",
        "landscape.png"
    ]
    for i, img in enumerate(images):
        src = img.get_attribute("src")
        assert expected_files[i] in src
        assert img.is_displayed()

    driver.quit()
