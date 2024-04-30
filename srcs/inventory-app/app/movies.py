from sqlalchemy import Integer, String, create_engine
from sqlalchemy.orm import DeclarativeBase, mapped_column
import os

DB_USER=os.getenv('DB_USER')
DB_PASSWD=os.getenv('DB_PASSWD')
DB_HOST=os.getenv('DB_HOST')
DB=os.getenv('DB_NAME')
DB_PORT=5432


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

Base.metadata.create_all(engine)