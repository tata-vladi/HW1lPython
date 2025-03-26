from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def login_and_get_message(driver, username, password):
    # Найдём поле ввода username
    username_field = driver.find_element(By.ID, 'username')
    username_field.send_keys(username)

    # Найдём поле ввода password
    password_field = driver.find_element(By.ID, 'password')
    password_field.send_keys(password)

    # Найдём кнопку Login и нажмём её
    login_button = driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
    login_button.click()

    # Подождём пару секунд для загрузки страницы после авторизации
    time.sleep(2)

    # Найдём текст с зеленой плашки и выведем его в консоль
    success_message = driver.find_element(By.CSS_SELECTOR, '.flash.success').text
    print(success_message)


if __name__ == "__main__":
    driver = webdriver.Firefox()

    try:
        # Откроем страницу
        driver.get("http://the-internet.herokuapp.com/login")
        time.sleep(2)  # Подождём пару секунд для полной загрузки страницы

        # Выполним авторизацию и получим сообщение
        login_and_get_message(driver, "tomsmith", "SuperSecretPassword!")

    finally:
        driver.quit()  # Закроем браузер после выполнения