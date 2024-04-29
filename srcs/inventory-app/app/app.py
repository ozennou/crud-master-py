from flask import Flask
import requests

app = Flask(__name__)
 
app.register_blueprint(requests.bp)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=3000)