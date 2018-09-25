# -*- coding: utf-8 -*-
# Python imports.
from wtforms import Form, BooleanField, StringField, TextAreaField, PasswordField, validators, IntegerField

# Local imports.
from app import login

# Forms.
# Examform.
class examForm(Form):
    course_name = StringField('Kursnamn', [validators.Length(min=2, max=50)])
    course_code = StringField('Kurskod', [validators.Length(min=2, max=20)])
    university = StringField('Universitet', [validators.Length(min=2, max=50)])
    semester = StringField('Termin', [validators.Length(min=2, max=10)])
    questions = IntegerField('Antal Fragor', [validators.Required()])

class addQuestionForm(Form):
    question = StringField('Question description', [validators.Length(min=3, max=50)])
    answer_a = StringField('Type Answer A')
    answer_b = StringField('Type Answer B')
    answer_c = StringField('Type Answer C')
    answer_d = StringField('Type Answer D')
    answer_e = StringField('Type Answer E')

# Registerform.
class registerForm(Form):
    username = StringField('Username', [validators.Length(min=4, max=20)])
    email = StringField('Email Address', [validators.Length(min=6, max=50)])
    password = PasswordField('New Password', [
        validators.Required(),
        validators.EqualTo('confirm_password', message='Password must match!')
    ])
    confirm_password = PasswordField('Repeat Password')
    accept_tos = BooleanField('I accept the Terms of Service and Privacy Notice (updated Jan 22, 2015)', [validators.Required()])
    
# Loginform.
class loginForm(Form):
    username = StringField('Username', [validators.Length(min=4, max=20)])
    password = PasswordField('New Password', [validators.Length(min=4, max=50)])
    remember_me = BooleanField('Remember me?', [validators.Required()])
