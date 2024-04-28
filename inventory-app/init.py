from sqlalchemy import insert, delete, update, select
from sqlalchemy.orm import Session
from sqlalchemy.orm import sessionmaker
import movie

Session = sessionmaker(movie.engine)


def add_movie(title, description):
    sess = Session()
    sess.execute(insert(movie.movie).values(title=title, description=description))
    sess.commit()
    sess.close()

def select_movie(id=None, title=None):
    sess = Session()
    if id is None and title is None:
        results = sess.execute(select(movie.movie)).fetchall()
    elif title is None:
        results = sess.execute(select(movie.movie).where(movie.movie.id == id)).fetchall()
    else:
        results = sess.execute(select(movie.movie).where(movie.movie.title == title)).fetchall()
    sess.close()
    movies_list = []
    if results:
        for result in results:
            movies_list.append({'id': result[0].id, 'title': result[0].title, 'description': result[0].description})
        return movies_list
    else:
        return {'message': 'Movie not found'}

def update_movie(id, title=None, description=None):
    sess = Session()
    if title is None and description is None:
        return
    elif description is None:
        sess.execute(update(movie.movie).where(movie.movie.id == id).values(title=title))
    elif title is None:
        sess.execute(update(movie.movie).where(movie.movie.id == id).values(description=description))
    else:
        sess.execute(update(movie.movie).where(movie.movie.id == id).values(title=title, description=description))
    sess.commit()
    sess.close()

def delete_movies(id=None):
    sess = Session()
    if id is None:
        sess.execute(delete(movie.movie))
    else:
        sess.execute(delete(movie.movie).where(movie.movie.id == id))
    sess.commit()
    sess.close()

# for i in range(10):
#     add_movie(f"movie{i}", f"desc{i * i}")
