from telebot.types import Message

from diploma.config_data.config import DEFAULT_COMMANDS
from diploma.loader import bot

def register_handlers(bot):
    @bot.message_handler(commands=["help"])
    def bot_help(message: Message):
        text = [f"/{command} - {desk}" for command, desk in DEFAULT_COMMANDS]
        bot.reply_to(message, "\n".join(text))
