# coding: utf-8
# Python imports.
from flask import Flask, flash, Blueprint, render_template, request, redirect, url_for, session
from flask_login import current_user, login_user, logout_user, login_required

# Local imports.
from app import db
from forms import *
from app.models import *

# Values.
urls_blueprint = Blueprint("urls", __name__,)

# Routes.
# Index.
@urls_blueprint.route('/')
@urls_blueprint.route('/index')
def index():
    return render_template('home.html')

# Exams.
@urls_blueprint.route('/exam')
def exam():
    return render_template('home.html')

# Functions.
# Private functions.
# Adding values to database from form.
def add_to_database(_form):
    # Check for model, add data to object, save to database.
    pass

# Public functions.

# Add exam.
@urls_blueprint.route('/add_exam', methods=['GET','POST'])
def add_exam():
    form = ExamForm(request.form)

    if request.method == 'POST' and form.validate():
        course_name = form.course_name.data
        course_code = form.course_code.data
        university = form.university.data
        semester = form.semester.data
        session['questions'] = form.questions.data
        
        ex = Exam(course_name = course_name, course_code = course_code, university = university, semester = semester)
        db.session.add(ex)

        return redirect(url_for('.add_questions'))
    
    return render_template('add_exam.html', ExamForm = form)

# Add questions to your exams
@urls_blueprint.route('/add_questions', methods=['GET', 'SET'])
def add_questions():
    form = QuestionForm(request.form)
    question_list = []
    qs = session['questions']
    for i in range(session['questions']):
        question_list.append(form)
        question_list[i].question.value = ("Question: " + str(i + 1))
        print(question_list[i].question.value)

    
    # if shit gets validated the code below will run okay
    if request.method == 'POST' and validate_list(question_list):
        redirect(url_for('.home.html'))
        
        
    return render_template('add_questions.html', qlist = question_list)

# check the questions so nothing is fucky
def validate_list(question_list):

    for question in question_list:
        question.validate()

# Register user.
@urls_blueprint.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)

    if request.method == 'POST' and form.validate():
        username = form.username.data
        email = form.email.data
        password = form.password.data    

        # Creating user.
        user = User(username = username, email = email, password = password)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()

        flash('You are now registered and can log in', 'success')

        return redirect('/')
    
    return render_template('register.html', registerForm=form)

# User login.
@urls_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        flash("You're already logged in!")
        return redirect('/')

    form = LoginForm(request.form)
    
    if request.method == 'POST' and form.validate():
        user = User.query.filter_by(username=form.username.data).first()
        
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect('/login')
        
        login_user(user, remember=form.remember_me.data)
        
        return redirect('/')
    
    return render_template('login.html', title='Sign In', loginForm=form)

# User logout.
@urls_blueprint.route('/logout')
def logout():
    logout_user()
    return redirect('/')
