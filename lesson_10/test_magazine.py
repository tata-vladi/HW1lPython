from typing import Any, Generator

import pytest
from selenium import webdriver
from LoginPage import LoginPage
from ProductPage import ProductPage
from ShoppingCartPage import ShoppingCartPage
from CheckoutPage import CheckoutPage
import allure
from selenium.webdriver.chrome.webdriver import WebDriver


@pytest.fixture
def browser() -> Generator[WebDriver, Any, None]:
    """Создает экземпляр веб-драйвера Chrome.

    Returns:
        webdriver.Chrome: Экземпляр веб-драйвера.
    """
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


@allure.title("Тест проверки общей суммы на этапе оформления заказа")
@allure.description("Данный тест проверяет, что общая сумма при оформлении заказа соответствует ожидаемому значению.")
@allure.feature("Оформление заказа")
@allure.severity(allure.severity_level.CRITICAL)
def test_checkout_total(browser: webdriver.Chrome) -> None:
    """Тест проверки общей суммы при оформлении заказа.

    Args:
        browser (webdriver.Chrome): Экземпляр веб-драйвера.

    Returns:
        None
    """

    with allure.step("Открыть страницу входа"):
        browser.get("https://www.saucedemo.com")

    login_page = LoginPage(browser)
    with allure.step("Ввести имя пользователя и пароль"):
        login_page.enter_username("standard_user")
        login_page.enter_password("secret_sauce")
        login_page.click_login_button()

    product_page = ProductPage(browser)
    with allure.step("Добавить товары в корзину"):
        product_page.add_item_to_cart("sauce-labs-backpack")
        product_page.add_item_to_cart("sauce-labs-bolt-t-shirt")
        product_page.add_item_to_cart("sauce-labs-onesie")
        product_page.navigate_to_cart()

    shopping_cart_page = ShoppingCartPage(browser)
    with allure.step("Перейти к оформлению заказа"):
        shopping_cart_page.click_checkout_button()

    checkout_page = CheckoutPage(browser)
    with allure.step("Заполнить данные для оформления заказа"):
        checkout_page.input_first_name("Иван")
        checkout_page.input_last_name("Иванов")
        checkout_page.input_zip_code("12345")
        checkout_page.complete_order()

    with allure.step("Проверить общую сумму заказа"):
        assert checkout_page.get_total_amount() == 58.29