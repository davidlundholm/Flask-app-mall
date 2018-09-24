# coding: utf-8
# Python imports.
from flask import Flask, flash, Blueprint, render_template, request, redirect, url_for, session
from passlib.hash import sha256_crypt

# Local imports.
from forms import *
from models import *
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
# Adding values to database.
def add_to_database(table_data):
    # Check for model, add data to object, save to database.
    pass

# Add exam.
@urls_blueprint.route('/add_exam', methods=['GET','POST'])
def add_exam():
    form = examForm(request.form)

    if request.method == 'POST' and form.validate():
        course_name = form.course_name.data
        course_code = form.course_code.data
        university = form.university.data
        semester = form.semester.data
        session['questions'] = form.questions.data

        ex = Exam(course_name = course_name, course_code = course_code, university = university, semester = semester)
        db.session.add(ex)

        return redirect(url_for('.add_questions'))
    
    return render_template('add_exam.html', examForm = form)


@urls_blueprint.route('/add_questions', methods=['GET', 'SET'])
def add_questions():
    form = addQuestionForm(request.form)
    amountOfQuestions = session['questions'] 
    

    if request.method == 'POST' and form.validate():
        pass
    return render_template('add_questions.html', addQuestionForm = form)

# Register user.
@urls_blueprint.route('/register', methods=['GET', 'POST'])
def register():
    form = registerForm(request.form)

    if request.method == 'POST' and form.validate():
        username = form.username.data
        email = form.email.data
        password = sha256_crypt.encrypt(str(form.password.data))

        # Creating user.
        user = User(username = username, email = email, password = password)
        
        db.session.add(user)
        db.session.commit()

        flash('You are now registered and can log in', 'success')

        return redirect('/')
    
    return render_template('register.html', registerForm=form)
