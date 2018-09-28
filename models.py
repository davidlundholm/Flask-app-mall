# Python imports.
from sqlalchemy import Integer, String, Column, Boolean
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

# Local imports.
# from app import login_manager

# Values.
db = SQLAlchemy()

# Models.
# Exam.
class Exam(db.Model):
    id = Column(Integer, primary_key=True)
    course_name = Column(String(80), nullable=False)
    course_code = Column(String(10), nullable=False)
    university = Column(String(120), nullable=False)
    semester = Column(String(120), nullable=False)
    questions = db.relationship('Question', backref='exam')

    def __repr__(self):
        return '<ID: %r, Kurs: %r, Kurskod: %r>' % (self.id, self.name, self.course_code)

# Question.
class Question(db.Model):
    id = Column(Integer, primary_key=True)
    text = Column(String(300), unique=True, nullable=False)
    answers = db.relationship('Answer', backref='question')
    exam_id = Column(Integer, db.ForeignKey('exam.id'))

# Answer.
class Answer(db.Model):
    id = Column(Integer, primary_key=True)
    text = Column(String(300), unique=True, nullable=False)
    correct = Column(Boolean, default=False)
    question_id = Column(Integer, db.ForeignKey('question.id'))

# User.
class User(UserMixin, db.Model):
   id = Column(Integer, primary_key=True)
   username = Column(String(300), unique=True, nullable=False)
   email = Column(String(300), unique=True, nullable=False)
   password = Column(String(300), unique=True, nullable=False)

# Login.


