# -*- coding: utf-8 -*-
# Python imports.
from wtforms import Form, BooleanField, StringField, TextAreaField, PasswordField, validators, IntegerField, FieldList, FormField



# Forms.
# Exam Question Form
class QuestionForm(Form):


    question = TextAreaField('', [validators.Length(min=3, max=50)], render_kw={"placeholder": "Question description"})
    answer_a = StringField('',[validators.Length(min=3, max=50)], render_kw={"placeholder": "A"})
    answer_b = StringField('',[validators.Length(min=3, max=50)], render_kw={"placeholder": "A"})
    answer_c = StringField('',[validators.Length(min=3, max=50)], render_kw={"placeholder": "A"})
    answer_d = StringField('',[validators.Length(min=3, max=50)], render_kw={"placeholder": "A"})
    answer_e = StringField('',[validators.Length(min=3, max=50)], render_kw={"placeholder": "A"})

# Examform.
class ExamForm(Form):
    course_name = StringField('Kursnamn', [validators.Length(min=2, max=50)])
    course_code = StringField('Kurskod', [validators.Length(min=2, max=20)])
    university = StringField('Universitet', [validators.Length(min=2, max=50)])
    semester = StringField('Termin', [validators.Length(min=2, max=10)])
    questions = IntegerField('Antal Fragor', [validators.Required()])
    



# Registerform.
class RegisterForm(Form):
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
