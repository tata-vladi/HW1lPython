from typing import Any, Generator

import allure
from selenium import webdriver
from calculator_page import CalculatorPage
import pytest
from selenium.webdriver.chrome.webdriver import WebDriver


@pytest.fixture
def driver() -> Generator[WebDriver, Any, None]:
    """Создает экземпляр веб-драйвера Chrome и завершает его после теста."""
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@allure.title("Тест калькулятора")
@allure.description("Проверка работы калькулятора с задержкой")
@allure.feature("Калькулятор")
@allure.severity(allure.severity_level.NORMAL)
def test_calculator(driver: webdriver.Chrome) -> None:
    """Тестирует функциональность калькулятора на веб-странице.

    Параметры:
        driver (webdriver.Chrome): Экземпляр веб-драйвера.

    Возвращаемое значение:
        None
    """
    calculator_page = CalculatorPage(driver)

    with allure.step("Открыть страницу калькулятора"):
        calculator_page.open_page("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    with allure.step("Ввести значение задержки"):
        calculator_page.enter_delay_value("45")

    with allure.step("Нажать на кнопку '7'"):
        calculator_page.click_button("7")

    with allure.step("Нажать на оператор '+'"):
        calculator_page.click_operator_button("+")

    with allure.step("Нажать на кнопку '8'"):
        calculator_page.click_button("8")

    with allure.step("Нажать на кнопку '='"):
        calculator_page.click_equals_button()

    with allure.step("Проверить результат"):
        assert calculator_page.get_result_text() == "15"


