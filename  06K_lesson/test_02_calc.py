import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_calculator_result(self):
        # Шаг 1: Открываем страницу
        url = 'https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html'
        self.driver.get(url)

        # Шаг 2: Вводим задержку 45 секунд
        delay_input = self.driver.find_element(By.ID, 'delay')
        delay_input.clear()
        delay_input.send_keys('45')

        # Шаг 3: Нажимаем на кнопки калькулятора
        buttons = {
            '7': (By.CSS_SELECTOR, "button[onclick='r(7)']"),
            '+': (By.CSS_SELECTOR, "button[onclick='r(\'+\')']"),
            '8': (By.CSS_SELECTOR, "button[onclick='r(8)']"),
            '=': (By.CSS_SELECTOR, "button[onclick='r(\'=\')']"),
        }

        for key, locator in buttons.items():
            button = self.driver.find_element(*locator)
            button.click()

        # Шаг 4: Ждем появления результата
        WebDriverWait(self.driver, 60).until(
            EC.text_to_be_present_in_element((By.ID, 'result'), '15')
        )

        # Шаг 5: Проверяем результат вычисления
        result = self.driver.find_element(By.ID, 'result').text
        self.assertEqual(result, '15', 'Результат вычисления неверен.')


if __name__ == '__main__':
    unittest.main()