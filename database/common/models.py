from peewee import Model, CharField, IntegerField, AutoField, BooleanField, ForeignKeyField
from diploma.database.core import db

class BaseModel(Model):
    class Meta:
        database = db

class User(BaseModel):
    user_id = IntegerField(unique=True)
    username = CharField()

class MovieSearchHistory(BaseModel):
    task_id = AutoField()
    user = ForeignKeyField(User, backref="tasks")
    movie_title = CharField()
    result = CharField()
    is_done = BooleanField(default=False)

    def __str__(self):
        return "{task_id}. {movie_title}".format(
            task_id=self.task_id,
            check="[V]" if self.is_done else "[ ]",
            movie_title=self.movie_title,
        )

db.connect()
db.create_tables([User, MovieSearchHistory])


