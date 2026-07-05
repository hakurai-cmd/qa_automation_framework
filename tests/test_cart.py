import pytest
from pages.login_page import LoginPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage
import allure

@allure.feature("Корзина")
@allure.story("Взаимодействие с товарами в корзине")
class TestCart:

    @allure.title("Добавление товара в корзину и проверка вложенности")
    @pytest.mark.regression
    def test_add_to_cart_and_verify(self, driver, test_data):
        login_page = LoginPage(driver)
        product_page = ProductPage(driver)
        cart_page = CartPage(driver)

        # 1. Авторизация
        login_page.open(test_data["env"]["base_url"])
        login_page.login(
            test_data["users"]["standard_user"]["username"],
            test_data["users"]["standard_user"]["password"]
        )

        # 2. Добавление товара (имя берем из нашего test_data.json)
        target_product = test_data["products"]["backpack_name"]
        product_page.add_product_to_cart(target_product)

        # 3. Проверка: счетчик на корзине стал равен "1"
        assert product_page.get_cart_badge_value() == "1", \
            "Счетчик корзины не обновился после добавления товара"

        # 4. Переход в корзину
        product_page.go_to_cart()

        # 5. Проверка: товар с нашим именем присутствует в корзине
        products_in_cart = cart_page.get_all_product_names_in_cart()
        assert target_product in products_in_cart, \
            f"Товар '{target_product}' не найден в корзине. Текущие товары: {products_in_cart}"