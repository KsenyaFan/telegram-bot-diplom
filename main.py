# from loader import bot
from utils.set_bot_commands import set_default_commands
from handlers.default_handlers import start, help, hello_world
from handlers.custom_handlers import command, history
from loader import bot

bot = bot


def register_handlers():
    start.register_handlers(bot)
    help.register_handlers(bot)
    hello_world.register_handlers(bot)
    command.register_handlers(bot)
    history.register_handlers(bot)


register_handlers()

if __name__ == "__main__":
    set_default_commands(bot)
    print("Запускаю бота...")
    bot.infinity_polling(none_stop=True)
    print("Бот запущен!")
