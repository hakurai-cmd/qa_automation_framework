# QA Automation Framework (Python + Selenium)

Профессиональный гибридный фреймворк для автоматизации тестирования UI и API. Построен по паттерну Page Object Model (POM) с использованием Data-Driven подхода.

## 🛠 Технологический стек
* **Язык:** Python 3.12
* **Тест-раннер:** Pytest (Маркеры, Фикстуры)
* **UI Автоматизация:** Selenium WebDriver (Explicit Waits)
* **API Тестирование:** Requests (Custom API Client)
* **Репорты:** Allure Framework + Интеграция с CI/CD
* **Логирование:** Loguru
* **Инфраструктура:** Docker, Docker Compose, GitHub Actions (CI/CD)

## 📁 Структура проекта

    qa_automation_framework/
    ├── .github/
    │   └── workflows/
    │       └── main.yml           # CI/CD пайплайн (GitHub Actions)
    ├── data/
    │   └── test_data.json         # Тестовые данные (логины, товары)
    ├── pages/                     # Page Object Model (POM)
    │   ├── base_page.py           # Общие методы для всех страниц
    │   ├── login_page.py
    │   ├── cart_page.py
    │   └── product_page.py
    ├── tests/                     # Тестовые сценарии
    │   ├── conftest.py            # Фикстуры (setup/teardown драйвера)
    │   ├── test_login.py          # Smoke-тесты
    │   ├── test_cart.py           # Регресс-тесты
    │   └── test_api.py            # API-тесты (Requests)
    ├── utils/                     # Хелперы и утилиты
    │   ├── logger.py              # Настройка логирования (Loguru)
    │   └── api_client.py          # Обертка над Requests
    ├── .env.example               # Образец конфигурационного файла
    ├── .gitignore
    ├── docker-compose.yml         # Запуск тестов в контейнерах
    ├── Dockerfile                 # Образ с окружением и зависимостями
    ├── pytest.ini                 # Конфигурация Pytest (пути, маркеры)
    ├── requirements.txt           # Список зависимостей
    └── README.md                  # Документация проекта

## 🚀 Как запустить локально

1. **Клонируйте репозиторий:**
   git clone https://github.com/hakurai-cmd/qa_automation_framework.git

2. **Настройте окружение:**
   Скопируйте .env.example в .env и укажите конфигурационные данные.

3. **Установите зависимости:**
   pip install -r requirements.txt

4. **Запустите тесты:**
   python -m pytest

5. **Сгенерируйте и откройте Allure-отчет:**
   allure serve allure-results

## 🐳 Запуск в Docker
Для изолированного запуска тестов в контейнере выполните команду:
docker-compose up --build