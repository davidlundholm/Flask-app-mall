# -*- coding: utf-8 -*-
# Python imports.
from wtforms import Form, StringField, TextAreaField, PasswordField, validators, IntegerField

# Forms.
# Examform.
class examForm(Form):
    course_name = StringField('Kursnamn', [validators.Length(min=2, max=50)])
    course_code = StringField('Kurskod', [validators.Length(min=2, max=20)])
    university = StringField('Universitet', [validators.Length(min=2, max=50)])
    semester = StringField('Termin', [validators.Length(min=2, max=10)])
    questions = IntegerField('Antal Fragor', [validators.Required()])

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
    
class examQuestions(Form)
