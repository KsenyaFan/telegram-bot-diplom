from telebot.states import State, StatesGroup

class MyStates(StatesGroup):
    name = State()
    age = State()
    color = State()
    hobby = State()