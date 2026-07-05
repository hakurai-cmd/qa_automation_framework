import os
import json
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# ФИКСТУРА 1: Загрузка тестовых данных из JSON
@pytest.fixture(scope="session")
def test_data():
    """Читает JSON-файл один раз за весь запуск тестов (scope='session')"""
    # Вычисляем абсолютный путь к файлу, чтобы Pytest нашел его и локально, и в GitHub Actions
    current_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(current_dir)
    data_path = os.path.join(project_root, "data", "test_data.json")
    
    with open(data_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data


# ФИКСТУРА 2: Инициализация и закрытие браузера
@pytest.fixture(scope="function")
def driver():
    """Запускает браузер перед каждым тестом (scope='function') и закрывает после"""
    options = Options()
    
    # Продвинутая фишка для CI/CD (GitHub Actions):
    # Если тесты запущены на сервере GitHub, там переменная окружения CI всегда равна true.
    # В этом случае принудительно включаем Headless-режим (без графического окна).
    if os.getenv("CI") == "true":
        options.add_argument("--headless=new")
    
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    # Старт браузера
    browser = webdriver.Chrome(options=options)
    
    yield browser # Здесь conftest ставит тест "на паузу" и отдает браузер в сам тест
    
    # Код после yield выполнится СТРОГО после завершения теста (Teardown)
    browser.quit()