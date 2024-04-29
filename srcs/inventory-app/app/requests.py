from flask import Blueprint, request
import db

bp = Blueprint('movies', __name__)

@bp.route('/api/movies/', defaults={'id': None}, methods=['GET'])
@bp.route('/api/movies/<int:id>', methods=['GET'])
def get_movies(id):
    title = request.args.get('title')
    if title:
        return db.select_movie(None, title)
    elif id:    
        return db.select_movie(id)
    else:
        return db.select_movie()

@bp.route('/api/movies/', methods=['POST'])
def post_movie():
    data = request.json
    if 'title' not in data or 'description' not in data:
        return {'message': 'specify the movie title and description'}, 400
    db.add_movie(data['title'], data['description'])
    return {'message': 'movie added successfully'}, 201

@bp.route('/api/movies/', defaults={'id': None}, methods=['DELETE'])
@bp.route('/api/movies/<int:id>', methods=['DELETE'])
def delete_movie(id):
    delete = db.delete_movies(id)
    if delete:
        return {'message': 'movie deleted successfully'}, 200
    else:
        return {'message': 'movie Not found'}, 400

@bp.route('/api/movies/<int:id>', methods=['PUT'])
def put_movie(id):
    data = request.json
    if 'title' not in data and 'description' not in data:
        return {'message': 'specify the movie title and description'}, 400
    if db.select_movie(id)[1] == 200:
        if 'title' in data and 'description' in data:
            db.update_movie(id, data['title'], data['description'])
        elif 'title' in data:
            db.update_movie(id, data['title'])
        else:
            db.update_movie(id, None, data['description'])
        return {'message': 'movie updated successfully'}, 200
    else:
        return {'message': 'movie Not found'}, 400