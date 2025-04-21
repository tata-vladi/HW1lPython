from selenium.webdriver.common.by import By

class ShoppingCartPage:
    def __init__(self, driver):
        self.driver = driver

    # Локаторы элементов
    CHECKOUT_BUTTON = (By.ID, 'checkout')
    ITEM_NAMES_IN_CART = (By.CLASS_NAME, 'inventory_item_name')

    def get_cart_items_names(self):
        """ Возвращает список наименований товаров, находящихся в корзине. """
        items_in_cart = []
        for element in self.driver.find_elements(*self.ITEM_NAMES_IN_CART):
            items_in_cart.append(element.text.strip())
        return items_in_cart

    def click_checkout_button(self):
        """ Нажимает кнопку Checkout для начала оформления заказа. """
        self.driver.find_element(*self.CHECKOUT_BUTTON).click()