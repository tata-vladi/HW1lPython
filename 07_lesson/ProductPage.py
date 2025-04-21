from selenium.webdriver.common.by import By

class ProductPage:
    def __init__(self, driver):
        self.driver = driver

    # Локаторы элементов
    ADD_TO_CART_BACKPACK = (By.ID, 'add-to-cart-sauce-labs-backpack')
    ADD_TO_CART_BIKE_LIGHT = (By.ID, 'add-to-cart-sauce-labs-bike-light')
    ADD_TO_CART_ONESIE = (By.ID, 'add-to-cart-sauce-labs-onesie')
    SHOPPING_CART_LINK = (By.CLASS_NAME, 'shopping_cart_link')

    def add_item_to_cart(self, item_id):
        """ Метод добавляет указанный продукт в корзину. :param item_id: идентификатор элемента товара (например, 'sauce-labs-backpack', 'bike-light' и др.) """
        locator = (By.ID, f'add-to-cart-{item_id}')
        self.driver.find_element(*locator).click()

    def navigate_to_cart(self):
        """Переходит в корзину."""
        self.driver.find_element(*self.SHOPPING_CART_LINK).click()