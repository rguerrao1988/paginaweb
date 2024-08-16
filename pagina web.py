#localhost:5000
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "home page"
@app.route("/about")
def about():
    return "about page"
if __name__ == "__main__":
    app.run()


