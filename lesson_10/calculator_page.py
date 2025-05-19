from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    """Класс для представления страницы калькулятора."""

    def __init__(self, driver: webdriver.Chrome) -> None:
        """Инициализирует страницу калькулятора.

        Параметры:
            driver (webdriver.Chrome): Экземпляр веб-драйвера.

        Возвращаемое значение:
            None
        """
        self.driver = driver

    def open_page(self, url: str) -> None:
        """Открывает указанную URL-страницу калькулятора.

        Параметры:
            url (str): URL страницы для открытия.

        Возвращаемое значение:
            None
        """
        self.driver.get(url)

    def enter_delay_value(self, value: str) -> None:
        """Вводит значение задержки в соответствующее поле.

        Параметры:
            value (str): Значение задержки для ввода.

        Возвращаемое значение:
            None
        """
        delay_input = self.driver.find_element_by_id("delay")
        delay_input.send_keys(value)

    def click_button(self, button_value: str) -> None:
        """Нажимает на кнопку калькулятора.

        Параметры:
            button_value (str): Значение кнопки, на которую нужно нажать.

        Возвращаемое значение:
            None
        """
        button = self.driver.find_element_by_xpath(f"//button[text()='{button_value}']")
        button.click()

    def click_operator_button(self, operator: str) -> None:
        """Нажимает на оператор калькулятора.

        Параметры:
            operator (str): Оператор, на который нужно нажать.

        Возвращаемое значение:
            None
        """
        operator_button = self.driver.find_element_by_xpath(f"//button[text()='{operator}']")
        operator_button.click()

    def click_equals_button(self) -> None:
        """Нажимает на кнопку '='."""
        equals_button = self.driver.find_element_by_xpath("//button[text()='=']")
        equals_button.click()

    def get_result_text(self) -> str:
        """Получает текст результата вычисления.

        Возвращаемое значение:
            str: Текст результата.
        """
        result = self.driver.find_element_by_id("result")
        return result.text
