import pytest
from pages.login_page import LoginPage
import allure

@allure.feature("Авторизация") # Группировка для красивого отчета Allure
@allure.story("Позитивные и негативные кейсы логина")
class TestLogin:

    @allure.title("Успешный логин со стандартным пользователем")
    @pytest.mark.smoke # Маркер для быстрого запуска только критических тестов
    def test_successful_login(self, driver, test_data):
        login_page = LoginPage(driver)
        
        # Шаг 1: Открываем сайт (берём урл из JSON)
        login_page.open(test_data["env"]["base_url"])
        
        # Шаг 2: Логинимся (данные берём из JSON)
        login_page.login(
            test_data["users"]["standard_user"]["username"],
            test_data["users"]["standard_user"]["password"]
        )
        
        # Шаг 3: Проверка (Проверяем, что URL изменился и мы попали в каталог)
        assert "inventory.html" in driver.current_url, \
            f"Ожидался URL каталога, но текущий URL: {driver.current_url}"

    @allure.title("Ошибка при логине заблокированного пользователя")
    @pytest.mark.regression
    def test_locked_out_user_login(self, driver, test_data):
        login_page = LoginPage(driver)
        
        login_page.open(test_data["env"]["base_url"])
        login_page.login(
            test_data["users"]["locked_out_user"]["username"],
            test_data["users"]["locked_out_user"]["password"]
        )
        
        # Получаем текст ошибки через метод страницы
        error_text = login_page.get_error_text()
        
        # Проверяем, что на экране появилась правильная плашка об ошибке
        expected_error = "Epic sadface: Sorry, this user has been locked out."
        assert error_text == expected_error, \
            f"Текст ошибки не совпал. Ожидалось: '{expected_error}', а пришло: '{error_text}'"