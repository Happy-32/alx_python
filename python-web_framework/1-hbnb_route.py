"""
Starts a web server
"""
from flask import Flask

app = Flask(__name__)
"""
Creating the routes
"""
@app.route("/")
def homepage():
    return "Hello HBNB!"

@app.route("/hbnb")
def hbnb():
    return "HBNB"

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="5000")