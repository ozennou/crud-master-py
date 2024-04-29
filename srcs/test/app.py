from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

test = {
    1:{'name':'Clean car'},
    2:{'name':'Write blog'},
    3:{'name':'Start stream'},
}

class items(Resource):
    def get(self):
        return test
    
class item(Resource):
    def get(self, id):
        return test[id]

api.add_resource(items, '/')
api.add_resource(item, '/<int:id>')

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=3000)