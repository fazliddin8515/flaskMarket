from market import app, db
from flask import render_template
from market.models import Item


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


@app.route("/register")
def register_page():
    return render_template("register.html")
