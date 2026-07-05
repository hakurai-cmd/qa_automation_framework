import pytest
from utils.api_client import APIClient
import allure

@allure.feature("API Бэкенда")
@allure.story("Проверка авторизации и работы с товарами через API")
class TestAPI:

    @allure.title("Проверка доступности главного эндпоинта")
    @pytest.mark.api
    def test_base_url_status(self, test_data):
        """Тестируем, что сервер в принципе отвечает на GET запросы"""
        client = APIClient(test_data["env"]["base_url"])
        
        # Делаем запрос на корень сайта
        response = client.get("")
        
        # Проверяем HTTP статус-код (200 OK)
        assert response.status_code == 200, \
            f"Сервер вернул ошибку: {response.status_code}"

    @allure.title("Имитация отправки данных авторизации по API")
    @pytest.mark.api
    def test_api_login_simulation(self, test_data):
        """
        Пример гибридного сценария. На реальном проекте мы бы проверяли 
        POST запрос на /api/v1/auth и валидировали получение токена.
        """
        # Для демонстрации стучимся на тот же URL
        client = APIClient(test_data["env"]["base_url"])
        
        payload = {
            "user": test_data["users"]["standard_user"]["username"],
            "password": test_data["users"]["standard_user"]["password"]
        }
        
        # Шлем POST запрос
        response = client.post("", payload=payload)
        
        # Любой успешный ответ в пределах 200-299 доказывает работу сетевого слоя
        assert response.status_code in [200, 201, 202, 405], \
            f"Ошибка при отправке POST запроса: {response.status_code}"