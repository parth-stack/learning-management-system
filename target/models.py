from target import db
from datetime import datetime

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), unique=True, nullable=False)
    def __repr__(self):
        return '<User %r>' % self.username

class Test(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(50))
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(120))
    optionA = db.Column(db.String(20))
    optionB = db.Column(db.String(20))
    optionC = db.Column(db.String(20))
    optionD = db.Column(db.String(20))
    answer = db.Column(db.String(5), nullable=False)
    testId = db.Column(db.Integer)
    def __repr__(self):
        return '<Question %r>' % self.description