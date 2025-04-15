from telebot import TeleBot
from telebot.storage import StateMemoryStorage

from config_data.config import BOT_TOKEN


storage = StateMemoryStorage()
print("Импортируем loader.py...")
bot = TeleBot(token=BOT_TOKEN, state_storage=storage)



#
# if __name__ == "__main__":
#     app.run(port=5000)




