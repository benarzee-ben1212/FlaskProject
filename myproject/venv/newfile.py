from flask import Flask

app = Flask(__name__)

@app.route("/newword")
def hello_world():
    return "<p>Hello, World! new word here 2,3</p>"