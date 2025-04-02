from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Шаг 1: Переход на сайт
url = 'http://uitestingplayground.com/textinput'
driver = webdriver.Chrome()  # Замените Chrome на ваш браузер, если используете другой
driver.get(url)

# Шаг 2: Ожидание видимости элемента и указание текста в поле ввода
input_field = WebDriverWait(driver, 30).until(
    EC.visibility_of_element_located((By.ID, 'newButtonName'))
)
input_field.send_keys('SkyPro')

# Шаг 3: Нажимаем на синюю кнопку
button = driver.find_element(By.ID, 'newButtonName')
button.click()

# Шаг 4: Получаем текст кнопки и выводим в консоль
button_text = button.text
print(button_text)

# Закрытие браузера после завершения работы
driver.quit()