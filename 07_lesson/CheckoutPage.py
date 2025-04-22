from selenium.webdriver.common.by import By

class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver

    # Локаторы элементов
    FIRST_NAME_FIELD = (By.ID, 'first-name')
    LAST_NAME_FIELD = (By.ID, 'last-name')
    ZIP_CODE_FIELD = (By.ID, 'postal-code')
    FINISH_BUTTON = (By.ID, 'finish')
    TOTAL_AMOUNT_LABEL = (By.CLASS_NAME, 'summary_total_label')

    def input_first_name(self, first_name):
        """ Ввод имени покупателя. """
        self.driver.find_element(*self.FIRST_NAME_FIELD).send_keys(first_name)

    def input_last_name(self, last_name):
        """ Ввод фамилии покупателя. """
        self.driver.find_element(*self.LAST_NAME_FIELD).send_keys(last_name)

    def input_zip_code(self, zip_code):
        """ Ввод почтового индекса. """
        self.driver.find_element(*self.ZIP_CODE_FIELD).send_keys(zip_code)

    def complete_order(self):
        """ Завершение оформления заказа. """
        self.driver.find_element(*self.FINISH_BUTTON).click()

    def get_total_amount(self):
        """ Получает итоговую сумму заказа. """
        amount_text = self.driver.find_element(*self.TOTAL_AMOUNT_LABEL).text
        # Извлекаем числовое значение из текста типа "$X.YZ"
        return float(amount_text.replace("$", ""))