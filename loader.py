import telebot
from telebot.storage import StateMemoryStorage
from diploma.config_data.config import BOT_TOKEN
import os
from dotenv import load_dotenv


storage = StateMemoryStorage()
bot = telebot.TeleBot(token=BOT_TOKEN, state_storage=storage)
# print(await bot.get_webhook_info())





