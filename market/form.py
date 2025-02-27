from flask_wtf import FlaskForm  # type: ignore
from wtforms import StringField, EmailField, PasswordField, SubmitField  # type: ignore
from wtforms.validators import EqualTo, DataRequired, ValidationError  # type: ignore
from sqlalchemy import select
from market.models import User
from market import db


class RegisterForm(FlaskForm):
    def validate_username(self, username):
        stmt = select(User).where(User.username == username.data)
        user = db.session.execute(stmt).scalars().first()
        if user:
            raise ValidationError("Username already exist!")

    def validate_email_address(self, email_address):
        stmt = select(User).where(User.email_address == email_address.data)
        user = db.session.execute(stmt).scalars().first()
        if user:
            raise ValidationError("Email Address already exist!")

    username = StringField(label="User Name", validators=[DataRequired()])
    email_address = EmailField(label="Email Address", validators=[DataRequired()])
    password1 = PasswordField(label="Password", validators=[DataRequired()])
    password2 = PasswordField(
        label="Comfirm Password",
        validators=[EqualTo("password1"), DataRequired()],
    )
    submit = SubmitField(label="Create Account")


class LoginForm(FlaskForm):
    username = StringField(label="User Name: ", validators=[DataRequired()])
    password = PasswordField(label="Password: ", validators=[DataRequired()])
    submit = SubmitField(label="Log in")
