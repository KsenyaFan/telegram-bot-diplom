from telebot.states import State, StatesGroup


class MyStates(StatesGroup):
    movie_search = State()
    history = State()
    movies_by_rating = State()
    person_name = State()