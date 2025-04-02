from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Шаг 1: Переход на страницу
url = 'http://uitestingplayground.com/ajax'
driver = webdriver.Chrome()  # Замените Chrome на ваш браузер, если используете другой
driver.get(url)

# Шаг 2: Нажатие на синюю кнопку
button = driver.find_element(By.ID, 'ajaxButton')
button.click()

# Шаг 3: Получение текста из зеленой плашки
WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CLASS_NAME, 'bg-success')))
green_text = driver.find_element(By.CLASS_NAME, 'bg-success').text

# Шаг 4: Вывод текста в консоль
print(green_text)

# Закрытие браузера после завершения работы
driver.quit()
