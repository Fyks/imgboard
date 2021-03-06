from flask_wtf.form import FlaskForm
from wtforms import StringField, BooleanField, PasswordField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    openid = StringField('openid', validators=[DataRequired()])
    remember_me = BooleanField('remember_me', default=False)
