import requests
from telebot.types import Message
from diploma.loader import bot
from diploma.api.core import url, headers, params

command_history = []

# Команда поиска фильмов
@bot.message_handler(commands=['search'])
def search_movie(message: Message):
    command_history.append('/search')
    bot.reply_to(message, "Введите название фильма для поиска:")

    # Ждём следующего сообщения
@bot.message_handler(func=lambda msg: True)
def handle_movie_search(msg: Message):
    query = msg.text
    # Запрос к API Кинопоиска
    api_url = url + "/v1.4/movie/search?page=1&limit=10"
    response = requests.get(api_url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()
        if data['docs']:
        # Формируем список фильмов
            movies = "\n".join([f"{movie['name']} ({movie['year']})" for movie in data['docs'][:5]])
            bot.reply_to(msg, f"Результаты поиска:\n{movies}")
        else:
            bot.reply_to(msg, "Ничего не найдено.")
    else:
        bot.reply_to(msg, "Произошла ошибка при запросе к API.")

    # url = "https://api.kinopoisk.dev/v1.4/movie/search?page=1&limit=10"
    #
    # headers = {"accept": "application/json"}
    #
    # response = requests.get(url, headers=headers)
    #
    # print(response.text)