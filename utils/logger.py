import os
from loguru import logger

# Определяем путь к папке с логами в корне проекта
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(current_dir)
logs_dir = os.path.join(project_root, "logs")

# Создаем папку, если ее еще нет
os.makedirs(logs_dir, exist_ok=True)

# Настраиваем логер
logger.remove() # Убираем дефолтные настройки

# 1. Лог в консоль (красивый, цветной)
logger.add(
    import_sys_stdout := __import__("sys").stdout,
    format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level: <8}</level> | <cyan>{module}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>",
    level="INFO"
)

# 2. Лог в файл (записывается на диск, чтобы прикрепить к артефактам в CI/CD)
logger.add(
    os.path.join(logs_dir, "framework.log"),
    format="{time:YYYY-MM-DD HH:mm:ss} | {level: <8} | {module}:{function}:{line} - {message}",
    level="DEBUG",
    rotation="10 MB", # Как только файл разрастется до 10МБ, создастся новый
    retention="5 days" # Хранить логи только за последние 5 дней
)