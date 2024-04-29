from flask import Flask, request
from flask_restful import Api, Resource
import init

app = Flask(__name__)
api = Api(app)

class movies(Resource):
    def get(self, id=None):
        if id is None:
            return init.select_movie()
        else:
            return init.select_movie(id)
    def post(self):
        data = request.json
        if 'title' not in data or 'description' not in data:
            return ({'message': 'specify the movie title and description'})
        init.add_movie(data['title'], data['description'])
        return ({'message': 'movie added successfully'})
        
api.add_resource(movies, "/api/movies")
# api.add_resource(movies, "/api/movies/<int:id>")

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=3000)