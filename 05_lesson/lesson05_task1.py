from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time


def click_blue_button(driver):
    # Найдём синюю кнопку по CSS классу
    blue_button = driver.find_element(By.CSS_SELECTOR, '.btn.btn-primary')

    # Нажмем на кнопку
    blue_button.click()


if __name__ == "__main__":
    service = Service(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=options)

    try:
        # Откроем страницу
        driver.get("http://uitestingplayground.com/classattr")
        time.sleep(2)  # Подождём пару секунд для полной загрузки страницы

        # Вызов функции для нажатия на синюю кнопку
        click_blue_button(driver)

    finally:
        driver.quit()  # Закроем браузер после выполнения