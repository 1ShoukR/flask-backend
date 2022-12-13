from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABSAE_URI"] = 'sqlite:///book.sqlite'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=True)
    password = db.Column(db.String(120), nullabel=True)


class ToDO(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable = False)
    title = db.Column(db.String(120), nullable = False)
    description = db.Column(db.Text(), nullable = True)
    due_date = db.Column(db.Date, nullable = True)
    completed = db.Column(db.Boolean, nullable = False, default = False)
    order_of_to_do = db.Column(db.Integer, nullable = False, autoincrement = True)