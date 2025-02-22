from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, PasswordField, SubmitField
from wtforms.validators import EqualTo, DataRequired

class RegisterForm(FlaskForm):
    username = StringField(label="User Name", validators=[DataRequired()])
    email_address = EmailField(label="Email Address", validators=[DataRequired()])
    password1 = PasswordField(label="Password", validators=[DataRequired()])
    password2 = PasswordField(label="Comfirm Password", validators=[EqualTo(fieldname="password1"), DataRequired()])
    submit = SubmitField(label="Create Account")
