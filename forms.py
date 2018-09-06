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
