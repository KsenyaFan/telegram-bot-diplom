from telebot.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, InputMediaPhoto

from states.states import MyStates
from config_data.config import HOST_API, DATE_FORMAT
from api.util.api_collections import KinoPoiskAPI, api_key
from database.common.models import db, User, MovieSearchHistory
from database.util.CRUD import retrieve_user_history

url = HOST_API
api = KinoPoiskAPI(api_key=api_key)


def register_handlers(bot):
    @bot.message_handler(commands=['history'])
    def show_history(message: Message):
        print("команда history")
        user_id = message.from_user.id
        text, poster, keyboard = get_history_page(user_id, 0)

        bot.send_photo(message.chat.id, photo=poster, caption=text, reply_markup=keyboard)

        # if poster:
        #     bot.send_photo(message.chat.id, photo=poster, caption=text, reply_markup=keyboard)
        # else:
        #     bot.send_message(message.chat.id, caption=text, reply_markup=keyboard)

    def get_history_page(user_id, page):
        per_page = 1
        offset = page * per_page

        history_query = (MovieSearchHistory
                         .select()
                         .where(MovieSearchHistory.user == user_id)
                         .order_by(MovieSearchHistory.timestamp.desc())
                         .limit(per_page)
                         .offset(offset))

        total_records = MovieSearchHistory.select().where(MovieSearchHistory.user == user_id).count()
        print(f"Всего записей: {total_records}")

        if not history_query.exists():
            return "История пуста.", None, None

        text = ""
        poster = None
        for record in history_query:
            text += f"{record.timestamp.strftime('%Y-%m-%d %H:%M')}\n{record.movie_title}\n{record.result}\n\n"
            poster = record.poster_url

        keyboard = InlineKeyboardMarkup()
        if page > 0:
            keyboard.add(InlineKeyboardButton("◀️ Назад", callback_data=f"history_{page - 1}"))
        if total_records > offset + per_page:
            keyboard.add(InlineKeyboardButton("Вперед ▶️", callback_data=f"history_{page + 1}"))

        return text, poster, keyboard

    @bot.callback_query_handler(func=lambda call: call.data.startswith("history_"))
    def history_pagination(call):
        page = int(call.data.split("_")[1])
        text, poster, keyboard = get_history_page(call.from_user.id, page)

        if poster:
            bot.edit_message_media(
                media=InputMediaPhoto(poster, caption=text),
                chat_id=call.message.chat.id,
                message_id=call.message.message_id,
                reply_markup=keyboard
            )
        else:
            bot.edit_message_text(text, call.message.chat.id, call.message.message_id, reply_markup=keyboard)