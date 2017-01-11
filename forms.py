from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import DataRequired , Email , Length

class SignupForm(FlaskForm):
    first_name  =   StringField('First name' , validators=[DataRequired('Please enter your first name')])
    last_name   =   StringField('Last name'  , validators=[DataRequired('Please enter your last  name')])
    password    =   PasswordField('Password' , validators=[DataRequired('Please enter your password'),
                                                           Length(min=6 , message='Password must be 6 character or more.')])
    email       =   StringField('Email'      , validators=[DataRequired('Please enter your email') ,
                                                           Email('Enter your valid email')])
    submit      =   SubmitField('Sign up')