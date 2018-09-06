# Python imports.
from sqlalchemy import Integer, String, Column, Boolean
from flask_sqlalchemy import SQLAlchemy

# Values.
db = SQLAlchemy()

# Models.
# Exam.
class Exam(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    course_name = db.Column(db.String(80), nullable=False)
    course_code = db.Column(db.String(10), nullable=False)
    university = db.Column(db.String(120), nullable=False)
    semester = db.Column(db.String(120), nullable=False)
    questions = db.relationship('Question', backref='exam')

    def __repr__(self):
        return '<ID: %r, Kurs: %r, Kurskod: %r>' % (self.id, self.name, self.course_code)

# Question.
class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(300), unique=True, nullable=False)
    answers = db.relationship('Answer', backref='question')
    exam_id = db.Column(db.Integer, db.ForeignKey('exam.id'))

# Answer.
class Answer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(300), unique=True, nullable=False)
    correct = db.Column(db.Boolean, default=False)
    question_id = db.Column(db.Integer, db.ForeignKey('question.id'))

