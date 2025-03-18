import os
from dotenv import load_dotenv, find_dotenv

if not find_dotenv():
    exit("Переменные окружения не загружены т.к отсутствует файл .env")
else:
    load_dotenv()


BOT_TOKEN = os.getenv("BOT_TOKEN")
API_KEY = os.getenv("X-API-KEY")
HOST_API = os.getenv("HOST_API")

DB_PATH = 'lecture.db'

DEFAULT_COMMANDS = (
    ("start", "Запустить бота"),
    ("help", "Вывести справку"),
    ("helloworld", "Приветствие"),
    ("history", "Вывести историю запросов"),
    ("search", "Поиск фильма по названию"),
    ("movies_rating", "Поиск фильмов по рейтингу"),
    ("person_name", "Поиск актера по имени "),
)

