# coding: utf-8
# Python imports.
from flask import Flask, Blueprint, render_template, request, redirect

# Local imports.
from forms import examForm
from models import Exam, Question, Answer
from models import db

# Values.
urls_blueprint = Blueprint("urls", __name__,)

# Routes.
# Index.
@urls_blueprint.route('/')
def index():
    return render_template('home.html') 

# Exams.
@urls_blueprint.route('/exam')
def exam():
    return render_template('home.html')

# Functions.
# Add exam.
@urls_blueprint.route('/add_exam', methods=['GET','POST'])
def add_exam():
    form = examForm(request.form)

    if request.method == 'POST' and form.validate():
        course_name = form.course_name.data
        course_code = form.course_code.data
        university = form.university.data
        semester = form.semester.data
        amountOfQuestions = form.questions.data

        ex = Exam(course_name = course_name, course_code = course_code, university = university, semester = semester)
        db.session.add(ex)
        return redirect('/add_questions')
    
    return render_template('add_exam.html', examForm = form)

@urls_blueprint.route('/add_questions', methods=['GET', 'POST'])
def add_questions():
    form = QuestionForm 
