from flask import Flask


app = Flask(__name__)


@app.route("/")
def index():
    return "hello world"

@app.route("/xd")
def sup():
    return "sup bitch ass mf"


if __name__ == "__main__":
    app.run(debug = True)