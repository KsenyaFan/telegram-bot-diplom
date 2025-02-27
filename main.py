from loader import bot
import handlers  # noqa
from utils.set_bot_commands import set_default_commands
from diploma.api.core import site_api, url, headers, params
from diploma.database.common.models import History, db
from diploma.database.core import crud


db_write = crud.create()
db_read = crud.retrieve()

fact_by_number = site_api.get_math_fact()
fact_by_data = site_api.get_date_fact()

response = fact_by_number("GET", url, headers, params, 5, timeout=3)
# response = response.json()
data = [{"number": response.get("number"), "massage": response.get("text")}]
print(response.text)

db_write(db, History, data)

response = fact_by_data("GET", url, headers, params, "6", "21", timeout=3)
# response = response.json()

data = [{"number": response.get("year"), "massage": response.get("text")}]
db_write(db, History, data)

retrieved = db_read(db, History, History.number, History.messege)

for element in retrieved:
    print(element.number, element.message)


if __name__ == "__main__":
    set_default_commands(bot)
    bot.infinity_polling()
