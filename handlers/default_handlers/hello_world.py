from telebot.types import Message

# from loader import bot


# Команда приветствия
def register_handlers(bot):
    @bot.message_handler(commands=['helloworld'])
    def send_welcome(message: Message):
        bot.send_message(message.chat.id, "Hello World!")
