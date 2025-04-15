from telebot.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from datetime import datetime
import requests
import json

from states.states import MyStates
from config_data.config import HOST_API, DATE_FORMAT
from api.util.api_collections import KinoPoiskAPI, api_key
from database.common.models import db, User, MovieSearchHistory
from database.util.CRUD import save_search_history

url = HOST_API
api = KinoPoiskAPI(api_key=api_key)


def register_handlers(bot):
    @bot.message_handler(commands=['movie_search'])
    def movie_search(message: Message):
        """Хендлер - обработчик команды /movie_search"""
        bot.send_message(message.chat.id, "Введите название фильма для поиска:")
        bot.register_next_step_handler(message, movie_by_search)

    @bot.message_handler(commands=['movies_rating'])
    def movies_by_rating(message: Message):
        """Хендлер - обработчик команды /movies_rating"""
        bot.send_message(message.chat.id, "Введите рейтинг для поиска фильмов:")
        bot.register_next_step_handler(message, movie_by_rating)

    @bot.message_handler(commands='person_name')
    def person_name(message: Message):
        """Хендлер - обработчик команды /person_name"""
        bot.send_message(message.chat.id, "Введите имя актера:")
        bot.register_next_step_handler(message, person_by_name)

    # @bot.message_handler(state=MyStates.movie_search, func=lambda message: True)
    def movie_by_search(message: Message):
        """Хендлер, который срабатывает после выполнения запроса
        поиска по наименованию фильма"""
        title = message.text.strip()
        if not title:
            bot.reply_to(message, "Вы ничего не ввели. Пожалуйста, укажи название фильма.")
            bot.register_next_step_handler(message, movie_by_search)
            return

        result = api.search_movie(title)
        print(json.dumps(result, indent=4, ensure_ascii=False))

        if "error" in result:
            bot.reply_to(message, f"Ошибка: {result['message']}")
        else:
            films = result.get("docs", [])
            print(films)
            if not films:
                bot.reply_to(message, "Фильмов с таким названием не найдено.")
            else:
                keyboard = InlineKeyboardMarkup()
                for film in films:
                    film_name = film['name']
                    film_year = film['year']
                    film_id = film['id']
                    keyboard.add(InlineKeyboardButton(f"{film_name} ({film_year})",
                                                      callback_data=f"search_{film_id}")
                                 )

                bot.send_message(message.chat.id, "Выбери фильм:", reply_markup=keyboard)

    # @bot.message_handler(state=MyStates.movies_by_rating, func=lambda message: True)
    def movie_by_rating(message: Message):
        """Хендлер, который срабатывает после выполнения запроса поиска по рейтингу фильма"""
        title = message.text.strip()

        try:
            result = api.get_movies_by_rating(int(title))
            print(json.dumps(result, indent=4, ensure_ascii=False))

            if "error" in result:
                bot.reply_to(message, f"Ошибка: {result['message']}")
            else:
                films = result.get("docs", [])
                if not films:
                    bot.reply_to(message, "Фильмов с таким рейтингом не найдено.")
                else:
                    keyboard = InlineKeyboardMarkup()
                    for film in films:
                        film_name = film['name']
                        film_id = film['id']
                        keyboard.add(InlineKeyboardButton(film_name, callback_data=f"search_{film_id}"))

                    response_text = "Выбери фильм:"

                    bot.send_message(message.chat.id, response_text, reply_markup=keyboard)

        except ValueError:
            bot.reply_to(message, "Рейтинг - это число. Пожалуйста, попробуй еще раз")
            bot.register_next_step_handler(message, movie_by_rating)

        bot.delete_state(message.from_user.id, message.chat.id)

    @bot.callback_query_handler(func=lambda call: call.data.startswith("search_"))
    def callback_movie_by_search(call):
        """Хендлер, который срабатывает после выбора фильма"""
        movie_id = call.data.split("_", 1)[1]
        bot.answer_callback_query(call.id)

        movie(call.message, movie_id, call.from_user.id)

    def movie(message: Message, movie_id, user_id):
        result = api.get_movies_by_id(movie_id)
        print(json.dumps(result, indent=4, ensure_ascii=False))
        print(f"Колбэк от user_id: {user_id}")

        if "error" in result:
            bot.reply_to(message, f"Ошибка: {result['message']}")
        else:
            film = result.get("docs", [])[0]
            if not film:
                bot.reply_to(message, "Фильм не найден.")
                return

            text = "\n".join([f"{film['name']} ({film['year']}) \nРейтинг: {film['rating']['kp']}\n"
                              f"Страна: {', '.join(c['name'] for c in film['countries'])}"])

            response_text = "\n".join([f"{film['name']} ({film['year']}) \nРейтинг: {film['rating']['kp']}\n"
                                       f"Страны: {', '.join(c['name'] for c in film['countries'])}\n"
                                       f"Жанр: {', '.join(g['name'] for g in film['genres'])}"
                                       f"\n\nОписание: {film['description']}"]
                                      )

            if film['poster']['url']:
                bot.send_photo(message.chat.id, film['poster']['url'], caption=response_text, parse_mode="Markdown")
                save_search_history(user_id=user_id, movie_title=film['name'],
                                    result=text, poster_url=film['poster']['url'])
                print(film['name'], film['poster']['url'])

            else:
                bot.send_message(message.chat.id, response_text, parse_mode="Markdown")
                save_search_history(user_id=user_id, movie_title=film['name'],
                                    result=text, poster_url=' ')

    # @bot.message_handler(state=MyStates.person_name, func=lambda message: True)
    def person_by_name(message: Message):
        """Хендлер, который срабатывает после выполнения запроса поиска имени актера/режиссера"""
        title = message.text.strip()
        if not title:
            bot.reply_to(message, "Вы ничего не ввели.Пожалуйста, укажи имя актера.")
            bot.register_next_step_handler(message, person_by_name)
            return

        result = api.get_person_by_name(title)
        print(json.dumps(result, indent=4, ensure_ascii=False))

        if "error" in result:
            bot.reply_to(message, f"Ошибка: {result['message']}")
        else:
            data = result.get("docs", [])
            if not data:
                bot.reply_to(message, "Актеров с таким именем не найдено.")
            else:
                response_text = "\n".join(
                    [f"{d['name']}\nДата рождения: {datetime.fromisoformat(d['birthday'][:-1]).strftime('%d.%m.%Y')}, "
                     f"\nвозраст: {d.get('age', 'неизвестно')}, пол: {d['sex']}" for d in data]
                )
                save_search_history(user_id=message.from_user.id, movie_title=title, result=response_text,
                                    poster_url=data[0]['photo'])
                bot.send_photo(message.chat.id, data[0]['photo'], caption=response_text)

        bot.delete_state(message.from_user.id, message.chat.id)

# bot.polling(none_stop=True)
# print(api.movie_search("Анора"))
