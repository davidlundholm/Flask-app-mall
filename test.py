from flask import Flask
from sqlalchemy import Integer, String, Column, Boolean
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:password@localhost:3300/myflaskapp'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    pets = db.relationship('Pet', backref='owner')

class Pet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    owner_id = db.Column(db.Integer, db.ForeignKey('person.id'))

db.create_all()

david = Person(name = 'David')
pricken = Pet(name='Pricken', owner = david)
db.session.add(david)
db.session.add(pricken)
db.session.commit()

if __name__ == '__main__':
    app.run(debug=True)
