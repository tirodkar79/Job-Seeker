from flask_wtf import FlaskForm
from wtforms import TextField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length


class Essays(FlaskForm):
    essays = TextAreaField('Write Your Essay', validators=[DataRequired()], render_kw = {'style' :'width:560px', 'rows':'9'})

    style = {'style': 'width:160px; background-color: blue; border-width: 2px; color: white'}
    submit = SubmitField('Submit', render_kw=style)