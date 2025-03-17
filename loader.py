from telebot import TeleBot
from telebot.storage import StateMemoryStorage

from diploma.config_data.config import BOT_TOKEN

# print(f"Токен бота: {BOT_TOKEN[:10]}...")
storage = StateMemoryStorage()
print("Импортируем loader.py...")
bot = TeleBot(token=BOT_TOKEN, state_storage=storage)
print(storage)


#
# if __name__ == "__main__":
#     app.run(port=5000)




