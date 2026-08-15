from selenium import webdriver
from calculator_page import CalculatorPage


def test_calc():
    driver = webdriver.Chrome()
    driver.maximize_window()

    calc_page = CalculatorPage(driver)

    calc_page.open()
    calc_page.set_delay("45")
    calc_page.click_7()
    calc_page.click_plus()
    calc_page.click_8()
    calc_page.click_equals()

    result = calc_page.get_result()
    assert result == "15", f"Ожидалось '15', но получено '{result}'"

    driver.quit()
