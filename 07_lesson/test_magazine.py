import pytest
from selenium import webdriver
from login_page import LoginPage
from product_page import ProductPage
from shopping_cart_page import ShoppingCartPage
from checkout_page import CheckoutPage


@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_checkout_total(browser):
    browser.get("https://www.saucedemo.com")

    login_page = LoginPage(browser)
    login_page.enter_username("standard_user")
    login_page.enter_password("secret_sauce")
    login_page.click_login_button()

    product_page = ProductPage(browser)
    product_page.add_item_to_cart("sauce-labs-backpack")
    product_page.add_item_to_cart("sauce-labs-bolt-t-shirt")
    product_page.add_item_to_cart("sauce-labs-onesie")
    product_page.navigate_to_cart()

    shopping_cart_page = ShoppingCartPage(browser)
    shopping_cart_page.click_checkout_button()

    checkout_page = CheckoutPage(browser)
    checkout_page.input_first_name("Иван")
    checkout_page.input_last_name("Иванов")
    checkout_page.input_zip_code("12345")
    checkout_page.complete_order()

    assert checkout_page.get_total_amount() == 58.29