from telebot.types import Message

from config_data.config import DEFAULT_COMMANDS
from loader import bot


def register_handlers(bot):
    @bot.message_handler(commands=["help"])
    def bot_help(message: Message):
        text = "Доступные команды:\n\n" + "\n".join([f"/{command} - {desk}" for command, desk in DEFAULT_COMMANDS])
        bot.reply_to(message, text)
