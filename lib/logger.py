import logging
import os

# Определяем директорию для логов
LOG_DIR = "logs"
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

# Определяем путь к файлу логов в директории проекта
LOG_FILE = os.path.join(LOG_DIR, "test.log")

# Настройка базового логгера для записи в файл
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format='%(asctime)s %(levelname)s: %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

class Logger:
    @staticmethod
    def log_request(url, data, headers, method):
        logging.info(f"Request: {method} {url}\nData: {data}\nHeaders: {headers}")

    @staticmethod
    def log_response(response):
        logging.info(
            f"Response: {response.status_code} {response.url}\nResponse Body: {response.text}"
        )
