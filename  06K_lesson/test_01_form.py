from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
waiter = WebDriverWait(driver, 10)

#Заполнение формы

driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

pole_i = driver.find_element(By.XPATH, "/html/body/main/div/form/div[1]/div[1]/label/input").send_keys("Иван")
pole_f = driver.find_element(By.XPATH, "/html/body/main/div/form/div[1]/div[2]/label/input").send_keys("Петров")
pole_ad = driver.find_element(By.XPATH, "/html/body/main/div/form/div[2]/div[1]/label/input").send_keys("Ленина, 55-3")
pole_g = driver.find_element(By.XPATH, "/html/body/main/div/form/div[2]/div[3]/label/input").send_keys("Москва")
pole_s = driver.find_element(By.XPATH, "/html/body/main/div/form/div[2]/div[4]/label/input").send_keys("Россия")
pole_e = driver.find_element(By.XPATH, "/html/body/main/div/form/div[3]/div[1]/label/input").send_keys("test@skypro.com")
pole_t = driver.find_element(By.XPATH, "/html/body/main/div/form/div[3]/div[2]/label/input").send_keys("+7985899998787")
pole_j = driver.find_element(By.XPATH, "/html/body/main/div/form/div[4]/div[1]/label/input").send_keys("QA")
pole_k = driver.find_element(By.XPATH, "/html/body/main/div/form/div[4]/div[2]/label/input").send_keys("SkyPro")

#Нажатие кнопки
submit_button = driver.find_element(By.CSS_SELECTOR, "body > main > div > form > div:nth-child(5) > div > button").click()

#Проверка подсветки поля Zip code
pole_z = driver.find_element(By.CSS_SELECTOR, "#zip-code").get_attribute("class")
assert pole_z == "alert py-2 alert-danger"

if pole_z == "alert py-2 alert-danger":
    print ("Zip code красный")
else: print("Zip code ошибка")

# Проверка подсветки остальных полей
poles = ["#first-name", "#last-name", "#address", "#city", "#country", "#e-mail" ,"#phone", "#company"]
for pole in poles:
 pole = driver.find_element(By.CSS_SELECTOR, pole).get_attribute("class")
assert pole == "alert py-2 alert-success"

if pole == "alert py-2 alert-success" :
    print ("Остальные все зеленый")
else: print("ошибка")

driver.quit()