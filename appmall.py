from flask import Flask, render_template, flash, redirect, url_for, session, request, logging
from data import Articles
from flask_mysqldb import MySQL
from wtforms import Form, IntegerField, StringField, TextAreaField, PasswordField, validators, BooleanField
from passlib.hash import sha256_crypt
from functools import wraps

from app_start import *

# init MYSQL
mysql = MySQL(get_app())

# Index
@app.route('/')
def index():
    # Create cursor
    cur = mysql.connection.cursor()
    # Get exams
    result = cur.execute("SELECT * FROM exam")
    exams = cur.fetchall()
    return render_template('home.html', exams=exams)

    cur.close()


# About
@app.route('/about')
def about():
    return render_template('about.html')


#Single exam
@app.route('/exam/<string:id>/')
def article(id):
    # Create cursor
    cur = mysql.connection.cursor()

    # Get article
    result = cur.execute("SELECT * FROM exam WHERE id = %s", [id])

    exam = cur.fetchone()

    return render_template('exam.html', exam=exam)


# Register Form Class
class RegisterForm(Form):
    name = StringField('Name', [validators.Length(min=1, max=50)])
    username = StringField('Username', [validators.Length(min=4, max=25)])
    email = StringField('Email', [validators.Length(min=6, max=50)])
    password = PasswordField('Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords do not match')
    ])
    confirm = PasswordField('Confirm Password')


# User Register
@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        name = form.name.data
        email = form.email.data
        username = form.username.data
        password = sha256_crypt.encrypt(str(form.password.data))

        # Create cursor
        cur = mysql.connection.cursor()

        # Execute query
        cur.execute("INSERT INTO users(name, email, username, password) VALUES(%s, %s, %s, %s)", (name, email, username, password))

        # Commit to DB
        mysql.connection.commit()

        # Close connection
        cur.close()

        flash('You are now registered and can log in', 'success')

        return redirect(url_for('login'))
    return render_template('register.html', form=form)


# User login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Get Form Fields
        username = request.form['username']
        password_candidate = request.form['password']

        # Create cursor
        cur = mysql.connection.cursor()

        # Get user by username
        result = cur.execute("SELECT * FROM users WHERE username = %s", [username])

        if result > 0:
            # Get stored hash
            data = cur.fetchone()
            password = data['password']

            # Compare Passwords
            if sha256_crypt.verify(password_candidate, password):
                # Passed
                session['logged_in'] = True
                session['username'] = username

                flash('You are now logged in', 'success')
                return redirect(url_for('index'))
            else:
                error = 'Invalid login'
                return render_template('login.html', error=error)
            # Close connection
            cur.close()
        else:
            error = 'Username not found'
            return render_template('login.html', error=error)

    return render_template('login.html')

# Check if user logged in
def is_logged_in(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('Unauthorized, Please login', 'danger')
            return redirect(url_for('login'))
    return wrap

# Logout
@app.route('/logout')
@is_logged_in
def logout():
    session.clear()
    flash('You are now logged out', 'success')
    return redirect(url_for('login'))

class add_examForm(Form):
    course = StringField('Kursnamn', [validators.Length(min=2, max=50)])
    course_code = StringField('Kurskod', [validators.Length(min=2, max=20)])
    university = StringField('Universitet', [validators.Length(min=2, max=50)])
    semester = StringField('Termin', [validators.Length(min=2, max=10)])
    questions = IntegerField('Antal Frågor', [validators.Required()])

class add_questionForm(Form):
    question = StringField('Fråga', [validators.Length(min=2, max=200)])
    answerA = StringField('Svar A', [validators.Length(min=2, max=50)])
    correctAnswerA = BooleanField('Correct Answer?', default="unchecked")
    answerB = StringField('Svar B', [validators.Length(min=2, max=50)])
    correctAnswerB = BooleanField('Correct Answer?')
    answerC = StringField('Svar C')
    correctAnswerC = BooleanField('Correct Answer?')
    answerD = StringField('Svar D')
    correctAnswerD = BooleanField('Correct Answer?')
    answerE = StringField('Svar E')
    correctAnswerE = BooleanField('Correct Answer?')

# Add exam
@app.route('/add_exam', methods=['GET', 'POST'])
@is_logged_in
def add_exam():
    examForm = add_examForm(request.form)

    if request.method == 'POST' and examForm.validate() and questionForm.validate():
        course = examForm.course.data
        course_code = examForm.course_code.data
        university = examForm.university.data
        semester = examForm.semester.data
        amountOfQuestions = examForm.questions.data
        
        tentainfo = {'course' : course, 'course_code' : course_code,
         'university' : university, 'semester' : semester,
         'amountOfQuestions' : amountOfQuestions}
        # Create cursor

        return render_template('add_questions', tentainfo=tentainfo)

    return render_template('add_exam.html', examForm=examForm)

# Add Article
@app.route('/add_article', methods=['GET', 'POST'])
@is_logged_in
def add_article():
    form = ArticleForm(request.form)
    if request.method == 'POST' and form.validate():
        title = form.title.data
        body = form.body.data

        # Create Cursor
        cur = mysql.connection.cursor()

        # Execute
        cur.execute("INSERT INTO articles(title, body, author) VALUES(%s, %s, %s)",(title, body, session['username']))

        # Commit to DB
        mysql.connection.commit()

        #Close connection
        cur.close()

        flash('Article Created', 'success')

        return redirect(url_for('dashboard'))

    return render_template('add_article.html', form=form)


# Edit Article
@app.route('/edit_article/<string:id>', methods=['GET', 'POST'])
@is_logged_in
def edit_article(id):
    # Create cursor
    cur = mysql.connection.cursor()

    # Get article by id
    result = cur.execute("SELECT * FROM articles WHERE id = %s", [id])

    article = cur.fetchone()
    cur.close()
    # Get form
    form = ArticleForm(request.form)

    # Populate article form fields
    form.title.data = article['title']
    form.body.data = article['body']

    if request.method == 'POST' and form.validate():
        title = request.form['title']
        body = request.form['body']

        # Create Cursor
        cur = mysql.connection.cursor()
        #app.logger.info(title)
        # Execute
        cur.execute ("UPDATE articles SET title=%s, body=%s WHERE id=%s",(title, body, id))
        # Commit to DB
        mysql.connection.commit()

        #Close connection
        cur.close()

        flash('Article Updated', 'success')

        return redirect(url_for('dashboard'))

    return render_template('edit_article.html', form=form)

# Delete Article
@app.route('/delete_article/<string:id>', methods=['POST'])
@is_logged_in
def delete_article(id):
    # Create cursor
    cur = mysql.connection.cursor()

    # Execute
    cur.execute("DELETE FROM articles WHERE id = %s", [id])

    # Commit to DB
    mysql.connection.commit()

    #Close connection
    cur.close()

    flash('Article Deleted', 'success')

    return redirect(url_for('dashboard'))

if __name__ == '__main__':
    app.secret_key='secret123'
    app.run(debug=True)
