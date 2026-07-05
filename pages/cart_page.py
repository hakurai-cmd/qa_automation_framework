from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import allure

class CartPage(BasePage):
    # ЛОКАТОРЫ
    _CART_ITEM_NAME = (By.CLASS_NAME, "inventory_item_name")
    _CHECKOUT_BUTTON = (By.ID, "checkout")

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Получение названий всех товаров в корзине")
    def get_all_product_names_in_cart(self):
        """
        Ищет все элементы товаров в корзине и возвращает список их текстовых названий.
        Поскольку элементов может быть несколько, мы используем базовый find_element для проверки 
        присутствия, а затем собираем текст.
        """
        self.find_element(self._CART_ITEM_NAME) # Убеждаемся, что хотя бы один элемент появился
        elements = self.driver.find_elements(*self._CART_ITEM_NAME)
        return [el.text for el in elements]