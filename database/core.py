from diploma.database.util.CRUD import CURDInteface
from .common.models import db, History


db.connect()
db.create_tables([History])

crud = CURDInteface()

if __name__ == '__main__':
    crud()