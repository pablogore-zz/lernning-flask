from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField

class SignupForm(FlaskForm):
    first_name  =   StringField('First name')
    last_name   =   StringField('Last name')
    password    =   PasswordField('Password')
    email       =   StringField('Email')
    submit      =   SubmitField('Sign up')