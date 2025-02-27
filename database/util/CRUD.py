from typing import Dict, List, TypeVar
from peewee import ModelSelect
from ..common.models import db, ModelBase

T = TypeVar("T")

#Метод сохранения данных
def _store_data(db: db, model: T, *data: List[Dict]) -> None:
    with db.atonic():
        model.insert_many(*data).execute()

#Метод  данных
def _retrieve_all_data(db: db, model: T, *colluns: ModelBase) -> ModelSelect:
    with db.atonic():
        responce = model.select(*colluns)

    return responce

class CURDInteface():
    @staticmethod
    def create():
        return _store_data

    @staticmethod
    def retrieve():
        return _retrieve_all_data

if __name__ == '__main__':
    _store_data()
    _retrieve_all_data()
    CURDInteface()