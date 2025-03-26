from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def input_text_and_clear(driver, text):
    # Найдём поле ввода
    input_field = driver.find_element(By.CSS_SELECTOR, 'input[type="number"]')

    # Введём текст в поле
    input_field.send_keys(text)
    time.sleep(2)  # Подождём пару секунд для визуальной проверки

    # Очистим поле
    input_field.clear()
    time.sleep(2)  # Подождём пару секунд для визуальной проверки


if __name__ == "__main__":
    options = webdriver.FirefoxOptions()
    driver = webdriver.Firefox()

    try:
        # Откроем страницу
        driver.get("http://the-internet.herokuapp.com/inputs")
        time.sleep(2)  # Подождём пару секунд для полной загрузки страницы

        # Введём число "1000" и очистим поле
        input_text_and_clear(driver, "1000")

        # Введём число "999"
        input_text_and_clear(driver, "999")

    finally:
        driver.quit()  # Закроем браузер после выполнения