from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import allure

class ProductPage(BasePage):
    # ЛОКАТОРЫ
    # Динамический локатор для кнопки добавления товара по его названию
    _ADD_TO_CART_BUTTON_TEMPLATE = "//div[text()='{0}']/ancestor::div[@class='inventory_item_description']//button"
    _CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    _CART_LINK = (By.CLASS_NAME, "shopping_cart_link")

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Добавление товара '{product_name}' в корзину")
    def add_product_to_cart(self, product_name):
        """Формирует XPATH под конкретный товар и кликает 'Add to cart'"""
        # Подставляем имя товара в наш шаблон XPATH
        xpath_locator = (By.XPATH, self._ADD_TO_CART_BUTTON_TEMPLATE.format(product_name))
        self.click_element(xpath_locator)

    def get_cart_badge_value(self):
        """Возвращает число на иконке корзины (количество добавленных товаров)"""
        return self.get_element_text(self._CART_BADGE)

    @allure.step("Переход в корзину через иконку в шапке")
    def go_to_cart(self):
        """Кликает на иконку тележки для перехода на страницу корзины"""
        self.click_element(self._CART_LINK)