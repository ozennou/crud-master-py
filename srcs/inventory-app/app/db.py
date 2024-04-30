from sqlalchemy import insert, delete, update, select
from flask import jsonify
from sqlalchemy.orm import Session
from sqlalchemy.orm import sessionmaker
import movies

Session = sessionmaker(movies.engine)


def add_movie(title, description):
    sess = Session()
    sess.execute(insert(movies.movie).values(title=title, description=description))
    sess.commit()
    sess.close()

def select_movie(id=None, title=None):
    sess = Session()
    if id is None and title is None:
        results = sess.execute(select(movies.movie)).fetchall()
    elif title is None:
        results = sess.execute(select(movies.movie).where(movies.movies.id == id)).fetchall()
    else:
        results = sess.execute(select(movies.movie).where(movies.movies.title == title)).fetchall()
    sess.close()
    movies_list = []
    if results:
        for result in results:
            movies_list.append({'id': result[0].id, 'title': result[0].title, 'description': result[0].description})
        return jsonify(movies_list), 200
    else:
        return jsonify({'message': 'Movie not found'}), 400

def update_movie(id, title=None, description=None):
    sess = Session()
    if title is None and description is None:
        return
    elif description is None:
        sess.execute(update(movies.movie).where(movies.movies.id == id).values(title=title))
    elif title is None:
        sess.execute(update(movies.movie).where(movies.movies.id == id).values(description=description))
    else:
        sess.execute(update(movies.movie).where(movies.movies.id == id).values(title=title, description=description))
    sess.commit()
    sess.close()

def delete_movies(id=None):
    sess = Session()
    exit = True
    if id is None:
        sess.execute(delete(movies.movie))
    else:
        if select_movie(id)[1] == 200:
            sess.execute(delete(movies.movie).where(movies.movies.id == id))
        else:
            exit = False
    sess.commit()
    sess.close()
    return exit