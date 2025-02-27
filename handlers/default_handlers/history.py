from diploma.loader import bot
from telebot.types import Message


command_history = []

# Обработчик команды /history для вывода истории
@bot.message_handler(commands=['history'])
def show_history(message: Message):
    command_history.append('/history')
    if command_history:
        history_text = "\n".join(command_history)
        bot.reply_to(message, f"История команд:\n{history_text}")
    else:
        bot.reply_to(message, "История пуста.")

bot.polling(none_stop=True)