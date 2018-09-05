from flask import Flask, render_template, request
from models import db, Exam, Question, Answer
from wtforms import Form, StringField, TextAreaField, PasswordField, validators, IntegerField

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:password@localhost:3300/myflaskapp'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

with app.app_context():
    db.init_app(app)
    db.create_all()

@app.route('/')
def index():
    return render_template('home.html') 

@app.route('/exam')
def exam():
    return render_template('home.html')

@app.route('/add_exam', methods=['GET','POST'])
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
        db.session.commit()
        return render_template('home.html')
    
    return render_template('add_exam.html', examForm = form) 

class examForm(Form):
    course_name = StringField('Kursnamn', [validators.Length(min=2, max=50)])
    course_code = StringField('Kurskod', [validators.Length(min=2, max=20)])
    university = StringField('Universitet', [validators.Length(min=2, max=50)])
    semester = StringField('Termin', [validators.Length(min=2, max=10)])
    questions = IntegerField('Antal Frågor', [validators.Required()])


if __name__ == '__main__':
    app.run(debug=True)

