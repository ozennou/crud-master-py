from flask import Flask
import RequestResponse as RR 

app = Flask(__name__)
 
app.register_blueprint(RR.bp)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=80)