from telebot.types import Message
# from diploma.loader import bot
from keyboards.inline.buttons import movie_buttons
from database.common.models import db, User


def register_handlers(bot):
    @bot.message_handler(commands=["start"])
    def bot_start(message: Message):
        user, created = User.get_or_create(user_id=message.from_user.id,
                                           defaults={"username": message.from_user.full_name})

        if created:
            bot.reply_to(message, f"Привет, {user.username}!")
            bot.send_message(message.chat.id, f"\nЭтот бот предназначен для поиска фильмов по названию, рейтингу,"
                                              f"или для получения информации по имени актера/режиссера")
        else:
            bot.reply_to(message, f"С возвращением, {user.username}! 👋")
        bot.send_message(message.chat.id, f"\n\nЧтобы посмотреть список доступных команд"
                                          f"набери команду /help, либо перейди в меню 👇")
