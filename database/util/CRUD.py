from typing import List, Dict
from peewee import ModelSelect
from datetime import datetime
from ..core import db
from ..common.models import MovieSearchHistory, User


def store_data(model, data: Dict) -> None:
    """Сохранение записи в базу"""
    with db.atomic():
        model.create(**data)


def retrieve_user_history(user_id: int) -> ModelSelect:
    """Получение истории поиска конкретного пользователя"""
    return MovieSearchHistory.select().where(MovieSearchHistory.user_id == user_id) \
        .order_by(MovieSearchHistory.timestamp.desc())


def get_user(user_id: int) -> User:
    """Получение пользователя по user_id"""
    return User.get_or_none(User.user_id == user_id)


def save_search_history(user_id: int, movie_title: str, result: str, poster_url: str) -> None:
    """Сохранение истории поиска в базу"""
    try:
        user, created = User.get_or_create(user_id=user_id, defaults={"username": "Unknown"})

        store_data(MovieSearchHistory, {
            "user": user_id,
            "movie_title": movie_title,
            "result": result,
            "poster_url": poster_url,
            "timestamp": datetime.now()
        })

        history_count = MovieSearchHistory.select().where(MovieSearchHistory.user == user_id).count()

        if history_count > 10:
            oldest_records = (MovieSearchHistory
                              .select()
                              .where(MovieSearchHistory.user == user_id)
                              .order_by(MovieSearchHistory.timestamp.asc())
                              .limit(history_count - 10)
                              )

            for record in oldest_records:
                record.delete_instance()



    except Exception as e:
        print(f"Ошибка при сохранении: {e}")
