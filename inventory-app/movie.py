from sqlalchemy import Integer, String
from sqlalchemy.orm import DeclarativeBase, mapped_column

class Base(DeclarativeBase):
    pass

class movie(Base):
    __tablename__ = "movies"
    id = mapped_column(Integer, primary_key=True)
    title = mapped_column(String)
    description = mapped_column(String)
    def __init__(self, title, description):
        self.title = title
        self.description = description