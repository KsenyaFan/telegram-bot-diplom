from telebot.types import Message
# from diploma.loader import bot
from diploma.keyboards.inline.buttons import movie_buttons
from diploma.database.common.models import db, User

def register_handlers(bot):
    @bot.message_handler(commands=["start"])
    def bot_start(message: Message):
        user, created = User.get_or_create(user_id=message.from_user.id,
                                           defaults={"username": message.from_user.full_name})

        if created:
            bot.reply_to(message, f"Привет, {user.username}!")
        else:
            bot.reply_to(message, f"С возвращением, {user.username}! 👋")
        # bot.send_message(message.chat.id, f"Выберите действие:",
        #                  reply_markup=movie_buttons()
        #                  )

