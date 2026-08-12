from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_image_loading():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")
    WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element((By.ID, "text"), "Done!")
    )

    image1 = driver.find_element(By.ID, "compass")
    image2 = driver.find_element(By.ID, "calendar")
    image3 = driver.find_element(By.ID, "award")
    image4 = driver.find_element(By.ID, "landscape")

    images = [image1, image2, image3, image4]

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
