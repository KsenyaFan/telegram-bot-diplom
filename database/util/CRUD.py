from typing import List, Dict
from peewee import ModelSelect
from diploma.database.core import db
from diploma.database.common.models import MovieSearchHistory, User

def store_data(model, data: Dict) -> None:
    """Сохранение записи в базу"""
    with db.atomic():
        model.create(**data)

def retrieve_all_data(model) -> ModelSelect:
    """Получение всех записей из таблицы"""
    return model.select()

def get_user(user_id: int) -> User:
    """Получение пользователя по user_id"""
    return User.get_or_none(User.user_id == user_id)

def save_search_history(user_id: int, movie_title: str, result: str) -> None:
    """Сохранение истории поиска в базу"""
    user, created = User.get_or_create(user_id=user_id,
        defaults={"username": "Unknown"})
    store_data(MovieSearchHistory,{"user": user_id, "movie_title": movie_title, "result": result})