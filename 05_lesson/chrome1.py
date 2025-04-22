from time import sleep #импортировали метод из пакета
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
browser = webdriver.Chrome(
service=ChromeService(ChromeDriverManager().install()))

browser.get("http://the-internet.herokuapp.com/add_remove_elements/.")

sleep(5) #установили «засыпание» браузера на 5 секунд

# Пять раз кликаем на кнопку Add Element
add_button = browser.find_element(By.XPATH, "//button[text()='Add Element']")
for _ in range(5):
    add_button.click()
    sleep(1)  # Ждем появления элемента

# Собираем список кнопок Delete
delete_buttons = browser.find_elements(By.XPATH, "//button[text()='Delete']")

# Выводим на экран размер списка
print(f'Количество кнопок Delete: {len(delete_buttons)}')

# Закрываем браузер
browser.quit()