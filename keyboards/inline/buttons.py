from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

def movie_buttons():
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("Поиск фильма по названию 🎬", callback_data="search"))
    markup.add(InlineKeyboardButton("Поиск фильмов по рейтингу", callback_data="movies_rating"))
    markup.add(InlineKeyboardButton("Поиск актера по имени", callback_data="movies_rating"))
    markup.add(InlineKeyboardButton("История запросов 📜", callback_data="history"))
    return markup

