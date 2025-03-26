from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def click_blue_button(driver):
    # Используем явное ожидание для поиска синей кнопки
    blue_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'btn btn-primary')]"))
    )
    # Нажмем на кнопку
    blue_button.click()


if __name__ == "__main__":
    service = Service(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=options)

    try:
        # Откроем страницу
        driver.get("http://uitestingplayground.com/dynamicid")

        # Вызов функции для нажатия на синюю кнопку
        click_blue_button(driver)

    finally:
        driver.quit()  # Закроем браузер после выполнения

        #// button[contains( @


       # class , ""