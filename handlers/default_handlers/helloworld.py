from telebot.types import Message
from telebot import TeleBot
from diploma.loader import bot


bot: TeleBot = bot
print(type(bot))

# Команда приветствия
@bot.message_handler(commands=['helloworld'])
def send_welcome(message: Message):
    bot.send_message(message.chat.id, "Hello World!")
