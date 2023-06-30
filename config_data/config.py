import os
from dotenv import load_dotenv, find_dotenv

if not find_dotenv():
    exit("Переменные окружения не загружены т.к отсутствует файл .env")
else:
    load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
RAPID_API_KEY = os.getenv("RAPID_API_KEY")
DEFAULT_COMMANDS = (
    ("start", "Запустить бота"),
    ("help", "Вывести справку"),
    ("weather","Узнать прогноз погоды в любом городе"),
    ("low","Узнать минимальную температуру в любом городе за последние 7 дней"),
    ("high","Узнать максимальную температуру в любом городе за последние 7 дней")
)

