from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    # Локаторы элементов
    USERNAME_FIELD = (By.ID, 'user-name')
    PASSWORD_FIELD = (By.ID, 'password')
    LOGIN_BUTTON = (By.ID, 'login-button')

    def enter_username(self, username):
        """Метод для ввода имени пользователя."""
        self.driver.find_element(*self.USERNAME_FIELD).clear()
        self.driver.find_element(*self.USERNAME_FIELD).send_keys(username)

    def enter_password(self, password):
        """Метод для ввода пароля."""
        self.driver.find_element(*self.PASSWORD_FIELD).clear()
        self.driver.find_element(*self.PASSWORD_FIELD).send_keys(password)

    def click_login_button(self):
        """Метод для нажатия кнопки входа."""
        self.driver.find_element(*self.LOGIN_BUTTON).click()
