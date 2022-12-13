from flask import Flask, redirect, url_for, render_template, request, session, g
from models import db, User, ToDO
from flask_cors import CORS, cross_origin
import json
import os

# Flask
app = Flask(__name__)
CORS(app)
app.config['SECRET_KEY'] = '\xc6\x1f\xbb=1\xc6\xf9"\x1f\x9d\xe5\xf0\xeaT\xcb>V\x07\xcb\xd9\xed\x95>C'
app.config['DEBUG'] = True


# Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:Rahmin12@localhost:3306/to_do_list_v2'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['DEBUG'] = True
db.init_app(app)



@app.before_request
def before_request():
    print("This is before request")
    print("this is session", session)



@app.route("/")
def index():
    db.create_all()
    response = {
        "name": "Rahmin",
        "about": "Hello! I'm a full stack developer that loves python and javascript!"
    }
    return response


@app.route('/sign-up', methods=["POST"])
def sign_up():
    incoming_data = request.json
    print("this is incoming data", incoming_data)
    return "signed in!", incoming_data


if __name__ == "__main__":
    app.run(debug = True)