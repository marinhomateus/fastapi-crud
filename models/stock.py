import ormar
from config import database, metadata


class MainMeta(ormar.ModelMeta):
    metadata = metadata
    database = database


class Stock(ormar.Model):
    class Meta(MainMeta):
        tablename = "stocks"

    id: int = ormar.Integer(primary_key=True)
    name: str = ormar.String(max_length=100)
    ticker: str = ormar.String(max_length=10)
    company_id: str = ormar.String(max_length=20)
