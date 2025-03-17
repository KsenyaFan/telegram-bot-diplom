from telebot.types import Message

from diploma.states.states import MyStates
from diploma.config_data.config import HOST_API
from diploma.api.util.api_collections import KinoPoiskAPI, api_key
from diploma.database.common.models import db, User, MovieSearchHistory
from diploma.database.util.CRUD import save_search_history

from diploma.keyboards.inline.buttons import movie_buttons

url = HOST_API

command_history = []
request_history = []


def register_handlers(bot):
    # Обработчик команды /history для вывода истории
    @bot.message_handler(commands=['history'])
    def show_history(message: Message):
        print("📜 Вызван хендлер history")
        user_id = message.from_user.id
        history = MovieSearchHistory.select().where(MovieSearchHistory.user_id == user_id)

        if history.exists():
            history_text = "\n".join([f"{h.task_id}. {h.movie_title} — {h.result}" for h in history])
            bot.reply_to(message, f"История запросов:\n{history_text}")
        else:
            bot.reply_to(message, "История пуста.")

    @bot.message_handler(commands=['request_history'])
    def req_history(message: Message):
        print("📜 Вызван хендлер request_history")
        command_history.append('/request_history')
        if request_history:
            request_history_text = "\n".join(request_history)
            bot.reply_to(message, f"История запросов:\n{request_history_text}")
        else:
            bot.reply_to(message, "История пуста.")


    @bot.message_handler(commands=['search'])
    def search(message: Message):
        print("🔎 Вызван search_movie, устанавливаем состояние search")
        print(message.chat.id, message.from_user.id)
        command_history.append('/search')

        bot.send_message(message.chat.id, "Введите название фильма для поиска.")
        # new_task = MovieSearchHistory(**message["search"])
        # new_task.save()
        bot.register_next_step_handler(message, movie_search)
        bot.set_state(message.from_user.id, MyStates.search, message.chat.id)
        with bot.retrieve_data(message.from_user.id) as data:
            data["new_task"] = {"user_id": message.from_user.id}


    # @bot.message_handler(state=MyStates.search, func=lambda message: True)
    def movie_search(message: Message):

        title = message.text.strip()
        if not title:
            bot.reply_to(message, "Пожалуйста, укажи название фильма после команды.")
            return

        # new_task["new_task"]["title"] = message.text

        api = KinoPoiskAPI(api_key=api_key)  # Пример API
        result = api.search_movie(title)

        if "error" in result:
            bot.reply_to(message, f"Ошибка: {result['message']}")
        else:
            films = result.get("docs", [])
            if not films:
                bot.reply_to(message, "Фильмов с таким названием не найдено.")
            else:
                response_text = "\n".join(
                    [f"{film['name']} ({film['year']}) - Рейтинг: {film['rating']['kp']}" for film in films]
                )
                save_search_history(user_id=message.from_user.id, movie_title=title, result=response_text)
                bot.reply_to(message, response_text)

        bot.delete_state(message.from_user.id, message.chat.id)

    @bot.message_handler(commands=['movies_rating'])
    def movies_rating(message: Message):
        print("🔎 Вызван movies_rating, устанавливаем состояние movies_rating")
        print(message.chat.id, message.from_user.id)
        command_history.append('/movies_rating')

        bot.send_message(message.chat.id, "Введите рейтинг для поиска фильмов:")
        bot.register_next_step_handler(message, movie_by_rating)
        bot.set_state(message.from_user.id, MyStates.movies_rating, message.chat.id)
        print(f"Состояние установлено: {bot.get_state(message.from_user.id, message.chat.id)}")

    # @bot.message_handler(state=MyStates.search, func=lambda message: True)
    def movie_by_rating(message: Message):

        title = message.text.strip()
        if not title:
            bot.reply_to(message, "Пожалуйста, укажи рейтинг фильма после команды.")
            return

        api = KinoPoiskAPI(api_key=api_key)  # Пример API
        result = api.get_movies_by_rating(int(title))

        if "error" in result:
            bot.reply_to(message, f"Ошибка: {result['message']}")
        else:
            films = result.get("docs", [])
            if not films:
                bot.reply_to(message, "Фильмов с таким рейтингом не найдено.")
            else:
                response_text = "\n".join(
                    [f"{film['name']} ({film['year']}) - Рейтинг: {film['rating']['kp']}" for film in films]
                )
                save_search_history(user_id=message.from_user.id, movie_title=title, result=response_text)
                bot.reply_to(message, response_text)

        bot.delete_state(message.from_user.id, message.chat.id)


    @bot.message_handler(commands='person_name')
    def person_name(message: Message):
        print("🔎 Вызван person_name, устанавливаем состояние person_name")
        print(message.chat.id, message.from_user.id)
        bot.send_message(message.chat.id, "Введите актера:")
        bot.register_next_step_handler(message, person_by_name)
        # bot.set_state(message.from_user.id, MyStates.movies_rating, message.chat.id)
        print(f"Состояние установлено: {bot.get_state(message.from_user.id, message.chat.id)}")

    # @bot.message_handler(state=MyStates.search, func=lambda message: True)
    def person_by_name(message: Message):

        title = message.text.strip()
        if not title:
            bot.reply_to(message, "Пожалуйста, укажи актера после команды.")
            return

        api = KinoPoiskAPI(api_key=api_key)  # Пример API
        result = api.get_person_by_name(title)
        print("Ответ сервера:", result)

        if "error" in result:
            bot.reply_to(message, f"Ошибка: {result['message']}")
        else:
            data = result.get("docs", [])
            if not data:
                bot.reply_to(message, "Фильмов с таким актером не найдено.")
            else:
                response_text = "\n".join(
                    [f"{d['name']} - Дата рождения: {d.get('birthday', 'неизвестно')}, "
                     f"возраст - {d.get('age', 'неизвестно')}, "
                     f"количество фильмов - {len(d.get('movies.name', []))}" for d in data]
                )
                save_search_history(user_id=message.from_user.id, movie_title=title, result=response_text)
                bot.reply_to(message, response_text)

        # bot.delete_state(message.from_user.id, message.chat.id)





# bot.polling(none_stop=True)
# print(api.movie_search("Интерстеллар"))