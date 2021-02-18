from . import db

class Employee(db.Model):
    __tablename__ = 'employees'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(64))
    last_name = db.Column(db.String(64))
    national_id = db.Column(db.String(64), unique=True)
    phone_number = db.Column(db.String(64), unique=True)
    address = db.Column(db.Text)
    married = db.Column(db.Boolean)
    age = db.Column(db.Integer)
    income = db.Column(db.Integer)


