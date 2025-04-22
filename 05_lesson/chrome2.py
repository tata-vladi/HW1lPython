from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def click_blue_button(driver):
    # Используем WebDriverWait для ожидания появления кнопки
    blue_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Button')]"))
    )

    # Кликнем на кнопку
    blue_button.click()


if __name__ == "__main__":
    service = Service(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=options)

    try:
        for i in range(3):  # Запускаем скрипт три раза
            print(f"Запуск {i + 1}")

            # Откроем страницу
            driver.get("http://uitestingplayground.com/dynamicid")

            # Вызываем функцию для клика на синюю кнопку
            click_blue_button(driver)

    finally:
        driver.quit()  # Закрываем браузер после завершения работы