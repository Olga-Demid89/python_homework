from selenium import webdriver
from shop_pages import LoginPage, MainPage, CartPage, CheckoutPage


def test_shop():
    driver = webdriver.Firefox()
    driver.maximize_window()

    login_page = LoginPage(driver)
    main_page = MainPage(driver)
    cart_page = CartPage(driver)
    checkout_page = CheckoutPage(driver)

    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    main_page.add_backpack()
    main_page.add_bolt_tshirt()
    main_page.add_onesie()
    main_page.go_to_cart()

    cart_page.click_checkout()

    checkout_page.fill_checkout_form("Ольга", "Демидова", "123456")

    total_text = checkout_page.get_total_price()

    assert "58.29" in total_text, f"Ожидалась сумма $58.29, но на странице отображено: '{total_text}'"

    driver.quit()
