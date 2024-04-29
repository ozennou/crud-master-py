DB_USER='amine'
DB_PASSWD='passwd'
DB_HOST='inventory-db'
DB_PORT='5432'
DB='movies_db'

from sqlalchemy import Integer, String, create_engine
from sqlalchemy.orm import DeclarativeBase, mapped_column

engine = create_engine(f"postgresql://{DB_USER}:{DB_PASSWD}@{DB_HOST}:{DB_PORT}/{DB}")

class Base(DeclarativeBase):
    pass

class movie(Base):
    __tablename__ = "movies"
    id = mapped_column(Integer, primary_key=True)
    title = mapped_column(String, nullable=False)
    description = mapped_column(String, nullable=False)
    def __init__(self, title, description):
        self.title = title
        self.description = description
    # def test(self) -> str:
    #     return f"Movie (id: {self.id}, title{self.title})"

Base.metadata.create_all(engine)