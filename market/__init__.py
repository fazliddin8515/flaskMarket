from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///market.sqlite"
app.config["SECRET_KEY"] = "HM28nbz3MQ16DW6289UieJ5kZwNXJcGb"

db.init_app(app)

from market import models

with app.app_context():
    db.create_all()


from market import routes
