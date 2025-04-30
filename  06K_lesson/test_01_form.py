import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

# Тестовая функция
@pytest.mark.usefixtures("driver")
def test_fill_form(driver):
    # Открытие страницы
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    # Заполнение формы
    driver.find_element(By.NAME, "first-name").send_keys("Иван")
    driver.find_element(By.NAME, "last-name").send_keys("Петров")
    driver.find_element(By.NAME, "address").send_keys("Ленина, 55-3")
    driver.find_element(By.NAME, "city").send_keys("Москва")
    driver.find_element(By.NAME, "country").send_keys("Россия")
    driver.find_element(By.NAME, "e-mail").send_keys("test@skypro.com")
    driver.find_element(By.NAME, "phone").send_keys("+7985899998787")
    driver.find_element(By.NAME, "job-title").send_keys("QA")
    driver.find_element(By.NAME, "company").send_keys("SkyPro")

    # Нажатие кнопки
    driver.find_element(By.CSS_SELECTOR, "body > main > div > form > div:nth-child(5) > div > button").click()

    # Проверка подсветки поля Zip code
    pole_z = driver.find_element(By.CSS_SELECTOR, "#zip-code").get_attribute("class")
    assert pole_z == "alert py-2 alert-danger"

    # Проверка подсветки остальных полей
    poles = ["#first-name", "#last-name", "#address", "#city", "#country", "#e-mail", "#phone", "#company"]
    for pole in poles:
        pole_class = driver.find_element(By.CSS_SELECTOR, pole).get_attribute("class")
        assert pole_class == "alert py-2 alert-success"