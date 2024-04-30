from sqlalchemy import Integer, String, create_engine
from sqlalchemy.orm import DeclarativeBase, mapped_column
import os

DB_USER='amine'
DB_PASSWD='passwd'
DB_HOST='127.0.0.1'
DB='orders_db'
DB_PORT=5432

engine = create_engine(f"postgresql://{DB_USER}:{DB_PASSWD}@{DB_HOST}:{DB_PORT}/{DB}")

class Base(DeclarativeBase):
    pass

class orders(Base):
    __tablename__ = "orders" 
    id = mapped_column(Integer, primary_key=True)
    user_id = mapped_column(Integer)
    number_of_items = mapped_column(Integer)
    total_amount = mapped_column(Integer)
    def __init__(self, user_id, number_of_items, total_amount):
        self.user_id = user_id
        self.number_of_items = number_of_items
        self.total_amount = total_amount

Base.metadata.create_all(engine)