from peewee import Model, CharField, IntegerField, AutoField, BooleanField, ForeignKeyField, DateTimeField
import os
from datetime import datetime
from ..core import db



class BaseModel(Model):
    class Meta:
        database = db


class User(BaseModel):
    user_id = IntegerField(unique=True)
    username = CharField()


class MovieSearchHistory(BaseModel):
    task_id = AutoField()
    user: ForeignKeyField = ForeignKeyField(User, backref="tasks")
    movie_title = CharField()
    result = CharField()
    timestamp = DateTimeField(default=datetime.now)
    is_done = BooleanField(default=False)
    poster_url = CharField(null=True)

    def __str__(self):
        return "{timestamp} - {task_id}. {movie_title}\n📷 {poster_url}".format(
            timestamp=self.timestamp,
            task_id=self.task_id,
            check="[V]" if self.is_done else "[ ]",
            movie_title=self.movie_title,
            poster_url=self.poster_url or "Нет постера"
        )



# if os.path.exists("lecture.db"):
#     os.remove("lecture.db")
#
db.connect()
# db.create_tables([User, MovieSearchHistory])
# db.drop_tables([User, MovieSearchHistory])

db.create_tables([User, MovieSearchHistory])

print("✅ Таблицы пересозданы!")


