from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///market.sqlite"

db.init_app(app)


class Item(db.Model):  # type: ignore
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(nullable=False)
    barcode: Mapped[int] = mapped_column(nullable=False, unique=True)
    price: Mapped[int] = mapped_column(nullable=False)


with app.app_context():
    db.create_all()


@app.route("/")
@app.route("/home")
def home_page():
    return render_template("home.html")


@app.route("/market")
def market_page():
    items = [
        {"id": 1, "name": "Phone", "barcode": "893212299897", "price": 500},
        {"id": 2, "name": "Laptop", "barcode": "123985473165", "price": 900},
        {"id": 3, "name": "Keyboard", "barcode": "231985128446", "price": 150},
        {"id": 4, "name": "Strawbar", "barcode": "3259235345569", "price": 20},
    ]
    return render_template("market.html", items=items)
