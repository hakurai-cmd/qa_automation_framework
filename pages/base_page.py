from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import allure

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.timeout = 10  # Дефолтное время ожидания элементов

    def open(self, url):
        with allure.step(f"Открытие страницы: {url}"):
            self.driver.get(url)

    def find_element(self, locator, timeout=None):
        """Ищет элемент с явным ожиданием"""
        wait_time = timeout if timeout else self.timeout
        try:
            return WebDriverWait(self.driver, wait_time).until(
                EC.presence_of_element_located(locator),
                message=f"Элемент {locator} не найден за {wait_time} сек."
            )
        except TimeoutException as e:
            raise AssertionError(e)
    def get_element_text(self, locator, timeout=None):
        return self.find_element(locator, timeout).text
    def click_element(self, locator, timeout=None):
        """Ожидает кликабельности и кликает"""
        wait_time = timeout if timeout else self.timeout
        with allure.step(f"Клик по элементу: {locator}"):
            try:
                element = WebDriverWait(self.driver, wait_time).until(
                    EC.element_to_be_clickable(locator),
                    message=f"Элемент {locator} не стал кликабельным"
                )
                element.click()
            except TimeoutException as e:
                raise AssertionError(e)

    def enter_text(self, locator, text, timeout=None):
        """Очищает поле и вводит текст"""
        with allure.step(f"Ввод текста '{text}' в {locator}"):
            element = self.find_element(locator, timeout)
            element.clear()
            element.send_keys(text)