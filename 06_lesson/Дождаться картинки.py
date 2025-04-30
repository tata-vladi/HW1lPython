from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Шаг 1: Переход на сайт
url = 'https://bonigarcia.dev/selenium-webdriver-java/loading-images.html'
driver = webdriver.Chrome()  # Замените Chrome на ваш браузер, если используете другой
driver.get(url)

# Шаг 2: Ожидание загрузки всех изображений
images = WebDriverWait(driver, 30).until(
    EC.presence_of_all_elements_located((By.TAG_NAME, 'img'))
)

# Шаг 3: Проверка и получение значения атрибута src у третьей картинки
if len(images) > 2:
    third_image_src = images[2].get_attribute('src')
    print(third_image_src)
else:
    print("Третье изображение не найдено")

# Закрытие браузера после завершения работы
driver.quit()