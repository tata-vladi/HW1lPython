from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Инициализация драйвера
with webdriver.Chrome() as driver:
    waiter = WebDriverWait(driver, 30)

    driver.get("https://www.saucedemo.com/")

    # Авторизация
    waiter.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#user-name"))).send_keys("standard_user")
    driver.find_element(By.CSS_SELECTOR, "#password").send_keys("secret_sauce")
    driver.find_element(By.CSS_SELECTOR, "#login-button").click()

    # Выбор товара
    waiter.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack"))).click()
    driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt").click()
    driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie").click()

    # Вход в корзину
    driver.find_element(By.CSS_SELECTOR, "#shopping_cart_container > a > span").click()

    # Нажатие Checkout
    driver.find_element(By.CSS_SELECTOR, "#checkout").click()

    # Заполнение формы
    driver.find_element(By.CSS_SELECTOR, "#first-name").send_keys("Татьяна")
    driver.find_element(By.CSS_SELECTOR, "#last-name").send_keys("Турищева")
    driver.find_element(By.CSS_SELECTOR, "#postal-code").send_keys("404832")

    # Нажатие Continue
    driver.find_element(By.CSS_SELECTOR, "#continue").click()

    # Вывести значение
    total = waiter.until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, "#checkout_summary_container > div > div.summary_info > div.summary_total_label"))).text

    # Проверочка
    assert total == "Total: $58.29", "Ошибка: Итоговая сумма не совпадает"
    print("Итоговая сумма = $58.29")