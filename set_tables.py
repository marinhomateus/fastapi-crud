import sqlalchemy

from config import DATABASE_URL, metadata
from models.stock import Stock


def set_db(database_url=DATABASE_URL):
    engine = sqlalchemy.create_engine(database_url)
    metadata.drop_all(engine)
    metadata.create_all(engine)


if __name__ == "__main__":
    set_db()
