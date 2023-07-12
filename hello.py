# $ .venv\Scripts\activate (en windows)
# $ flask --app hello run
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p> introduzca el valor de a"