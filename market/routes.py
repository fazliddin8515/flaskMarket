from market import app, db
from flask import render_template, redirect, url_for, flash
from market.models import Item, User
from market.form import RegisterForm, LoginForm
from sqlalchemy import select
from flask_login import login_user, logout_user  # type: ignore


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


@app.route("/register", methods=["GET", "POST"])
def register_page():
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(
            username=form.username.data,
            email_address=form.email_address.data,
            password=form.password1.data,
        )
        db.session.add(user)
        db.session.commit()
        login_user(user)
        flash(f"User registered in as {user.username}", "success")
        return redirect(url_for("market_page"))

    if form.errors != {}:
        for err_msg in form.errors.values():
            flash(err_msg, "danger")

    return render_template("register.html", form=form)


@app.route("/login", methods=["GET", "POST"])
def login_page():
    form = LoginForm()
    if form.validate_on_submit():
        stmt = select(User).where(User.username == form.username.data)
        user = db.session.execute(stmt).scalars().first()
        if user and user.check_password(form.password.data):
            login_user(user)
            flash(f"User logged in as {user.username}", "success")
            return redirect(url_for("market_page"))
        else:
            flash("Username and password are not matched!", "danger")

    return render_template("login.html", form=form)


@app.route("/logout")
def logout_page():
    logout_user()
    return redirect(url_for("login_page"))
