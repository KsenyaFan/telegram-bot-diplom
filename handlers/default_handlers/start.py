from telebot.types import Message
from telebot.states.sync.context import StateContext
from diploma.loader import bot

@bot.message_handler(commands=["start"])
def bot_start(message: Message, state: StateContext):
    bot.reply_to(message, f"Привет, {message.from_user.full_name}!")
