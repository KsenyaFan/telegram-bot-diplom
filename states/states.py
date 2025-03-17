from telebot.states import State, StatesGroup


class MyStates(StatesGroup):
    search = State()
    history = State()
    movies_rating = State()