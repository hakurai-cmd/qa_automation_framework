import requests
import allure
from utils.logger import logger

class APIClient:
    def __init__(self, base_url):
        self.base_url = base_url
        self.session = requests.Session() # Сессия сохраняет куки между запросами

    @allure.step("Отправка POST запроса на {endpoint}")
    def post(self, endpoint, payload=None, headers=None):
        url = f"{self.base_url}{endpoint}"
        logger.info(f"API POST Request to: {url} | Payload: {payload}")
        
        try:
            response = self.session.post(url, json=payload, headers=headers, timeout=10)
            logger.info(f"API Response Status: {response.status_code}")
            # Возвращаем объект ответа, чтобы в тесте проверить статус или забрать json
            return response
        except Exception as e:
            logger.error(f"API Request failed: {e}")
            raise e

    @allure.step("Отправка GET запроса на {endpoint}")
    def get(self, endpoint, params=None, headers=None):
        url = f"{self.base_url}{endpoint}"
        logger.info(f"API GET Request to: {url} | Params: {params}")
        
        try:
            response = self.session.get(url, params=params, headers=headers, timeout=10)
            logger.info(f"API Response Status: {response.status_code}")
            return response
        except Exception as e:
            logger.error(f"API Request failed: {e}")
            raise e