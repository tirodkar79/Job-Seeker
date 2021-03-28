from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, PasswordField, SelectField, SubmitField
from wtforms.validators import DataRequired, Length, EqualTo, NumberRange


class Login(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max= 30)])

    password = PasswordField('Password', validators=[DataRequired(), Length(min=2, max=20)])

    style = {'style': 'width:160px'}
    submit = SubmitField('Login', render_kw=style)
