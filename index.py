from flask import flask

app = flask(__name__)

@app.route('/')
def home():
    return "hello word"

if __name__ == "_main_":
    app.run()