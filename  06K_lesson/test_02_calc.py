import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_calculator_result(driver):
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/"
               "slow-calculator.html")

    # Установка задержки
    delay_input = driver.find_element(By.CSS_SELECTOR, "#delay")
    delay_input.clear()
    delay_input.send_keys("5")

    # Нажатие кнопок 7 + 8 =
    driver.find_element(By.XPATH, f'//span[text()="7"]').click()
    driver.find_element(By.XPATH, f'//span[text()="+"]').click()
    driver.find_element(By.XPATH, f'//span[text()="8"]').click()
    driver.find_element(By.XPATH, '//span[text()="="]').click()

    # Ожидание и проверка результата
    result = WebDriverWait(driver, 46).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), "15"))
    assert driver.find_element(By.CSS_SELECTOR, ".screen").text == "15"