from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from database.common.models import db, User, MovieSearchHistory

def movie_buttons(user_id, page=0):
    history = (MovieSearchHistory
               .select()
               .where(MovieSearchHistory.user == user_id)
               .order_by(MovieSearchHistory.timestamp.desc())
               .limit(10))

    if not history:
        return "История пуста.", None

    record = history[page]
    text = (f"{record.timestamp.strftime('%d.%m.%Y %H:%M')}\n"
            f"🎬 {record.movie_title}\n"
            f"📜 {record.result}")
    markup = InlineKeyboardMarkup()
    markup.row(*[InlineKeyboardButton(
        text=LEXICON[button] if button in LEXICON else button,
        callback_data=button) for button in buttons])
    return markup

