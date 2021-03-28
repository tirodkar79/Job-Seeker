from flask_wtf import FlaskForm
import email_validator
from wtforms import StringField, IntegerField, PasswordField, SelectField, SubmitField, FloatField, TextAreaField
from wtforms.validators import DataRequired, Length, EqualTo, NumberRange, Email


class Registration(FlaskForm):
    fname = StringField('First Name', validators=[
                         DataRequired(), Length(min=2, max=35)])
    lname = StringField('Last Name', validators=[
                         DataRequired(), Length(min=2, max=35)])
    email = StringField('Email Id', validators=[
                         DataRequired(), Length(min=2, max=35)])
    phone_no = IntegerField('Phone No.', validators=[DataRequired()])
    objective = TextAreaField('Objective', validators=[DataRequired()])
    hsc_name = StringField('College Name', validators=[DataRequired()])
    hsc_percent = FloatField('HSC Percentage', validators=[DataRequired()])
    college_name = StringField('University Name', validators=[DataRequired()])
    college_cgpa = FloatField('CGPA', validators=[DataRequired()])
    year = SelectField('Year', choices=[('SE', 'Second Year'), ('TE', 'Third Year'), ('FE', 'Fourth Year')], default="FE")
    project_name = StringField('Project Name', validators=[DataRequired()])
    project_desc = TextAreaField('Project Description', validators=[DataRequired()])
    skills = TextAreaField('One skill a line', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=5, max=12)])
    cpwd = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])

    style = {'style': 'width:160px'}
    submit = SubmitField('Submit', render_kw=style)
