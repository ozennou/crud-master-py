from sqlalchemy import create_engine, text, String, Table, MetaData, Column, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import DeclarativeBase, mapped_column

class Base(DeclarativeBase):
    pass

class movie(Base):
    __tablename__ = "table1"
    id = mapped_column(Integer, primary_key=True)
    title = mapped_column(String)
    description = mapped_column(String)
    def __init__(self, title, description):
        self.title = title
        self.description = description
    def __print__(self) ->str:
        return f"movie(id: {self.id}, title: {self.title}, desc: {self.description})"


DB_USER='amine'
DB_PASSWD='passwd'
DB_HOST='127.0.0.1'
DB_PORT='5432'
DB='test_db' #change to movies_db
# engine = create_engine("postgresql://amine:passwd@127.0.0.1:5432/test_db", echo=True)

# with Session(engine) as conn:
#     conn.execute(text('CREATE TABLE IF NOT EXISTS table1 (id SERIAL PRIMARY KEY, title VARCHAR(255) NOT NULL, description TEXT NOT NULL)'))
#     conn.commit()

engine = create_engine(f"postgresql://{DB_USER}:{DB_PASSWD}@{DB_HOST}:{DB_PORT}/{DB}", echo=True)

Session = sessionmaker(engine)

test = movie("adsfadsf", "asdfasdf")

print(test.__print__())

with Session() as sess:
    sess.add(test)
    sess.commit()

# delete_movies(25)