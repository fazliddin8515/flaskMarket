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

    def __repr__(self):
        return f"<Item (name: {self.name}, price: {self.price})>"


with app.app_context():
    db.create_all()


@app.route("/")
@app.route("/home")
def home_page():
    return render_template("home.html")


@app.route("/market")
def market_page():
    select_stmt = db.select(Item)
    result = db.session.execute(select_stmt)
    items = result.scalars().all()
    print(items)
    return render_template("market.html", items=items)
