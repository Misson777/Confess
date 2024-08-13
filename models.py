from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    city = db.Column(db.String(80), nullable=False)
    school = db.Column(db.String(80), nullable=False)
    gender = db.Column(db.String(10), nullable=False)

class Confession(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    crush_name = db.Column(db.String(80), nullable=False)
    crush_birthday = db.Column(db.Date, nullable=False)
    crush_city = db.Column(db.String(80), nullable=False)
    first_meet_place = db.Column(db.String(80), nullable=False)
    crush_school = db.Column(db.String(80), nullable=False)
    match_found = db.Column(db.Boolean, default=False)