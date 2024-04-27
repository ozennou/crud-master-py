DB_USER='amine'
DB_PASSWD='passwd'
DB_HOST='127.0.0.1'
DB_PORT='5432'
DB='movies_db'

from sqlalchemy import text, create_engine
from sqlalchemy.orm import Session
from sqlalchemy.orm import sessionmaker

# from sqlalchemy.orm import DeclarativeBase
# class Base(DeclarativeBase):
#     pass



engine = create_engine(f"postgresql://{DB_USER}:{DB_PASSWD}@{DB_HOST}:{DB_PORT}/{DB}", echo=True)

Session = sessionmaker(engine)

def add_movie(title, description):
    sess = Session()
    sess.execute(text(f"INSERT INTO table1 (title, description) VALUES(:title, :description)"), {"title": title, "description": description})
    sess.commit()

def delete_movies(id=None):
    sess = Session()
    if id is None:
        sess.execute(text("DELETE FROM table1"))
    else:
        sess.execute(text("DELETE FROM table1 WHERE id=:id"), {"id": id})
    sess.commit()

def update_movie(id, title=None, description=None):
    sess = Session()
    if title is None and description is None:
        return
    elif description is None:
        sess.execute(text("UPDATE table1 SET title=:title WHERE id=:id"), {"title": title, "id": id})
    elif title is None:
        sess.execute(text("UPDATE table1 SET description=:description WHERE id=:id"), {"description": description, "id": id})
    else:
        sess.execute(text("UPDATE table1 SET title=:title, description=:description WHERE id=:id"), {"title": title, "description": description, "id": id})
    sess.commit()


