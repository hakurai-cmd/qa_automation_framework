# Шаг 1: Берем официальный легкий образ Python
FROM python:3.11-slim

# Шаг 2: Устанавливаем в контейнер Linux-зависимости и Google Chrome для тестов
RUN apt-get update && apt-get install -y \
    wget \
    gnupg \
    unzip \
    google-chrome-stable \
    && rm -rf /var/lib/apt/lists/*

# Шаг 3: Создаем рабочую папку внутри контейнера
WORKDIR /app

# Шаг 4: Копируем файл с зависимостями и устанавливаем их
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Шаг 5: Копируем весь остальной код проекта в контейнер
COPY . .

# Шаг 6: Команда по умолчанию — запуск тестов с генерацией отчета Allure
CMD ["pytest", "tests/", "--alluredir=allure-results"]