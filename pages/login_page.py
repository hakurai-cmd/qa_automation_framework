from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import allure

class LoginPage(BasePage):
    # 1. ЛОКАТОРЫ СТРАНИЦЫ (хранятся строго тут)
    _USERNAME_INPUT = (By.ID, "user-name")
    _PASSWORD_INPUT = (By.ID, "password")
    _LOGIN_BUTTON = (By.ID, "login-button")
    _ERROR_MESSAGE = (By.CSS_SELECTOR, "h3[data-test='error']")

    def __init__(self, driver):
        super().__init__(driver)  # Инициализируем родительский BasePage

    # 2. БИЗНЕС-ЛОГИКА (Методы действия)
    @allure.step("Авторизация пользователя с логином '{username}'")
    def login(self, username, password):
        """Объединяет три низкоуровневых действия в один понятный шаг"""
        self.enter_text(self._USERNAME_INPUT, username)
        self.enter_text(self._PASSWORD_INPUT, password)
        self.click_element(self._LOGIN_BUTTON)

    def get_error_text(self):
        """Получает текст ошибки при неудачном логине"""
        return self.find_element(self._ERROR_MESSAGE).text