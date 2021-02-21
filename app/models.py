from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from . import login_manager


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class Employee(db.Model):
    __tablename__ = 'employees'
    id = db.Column(db.Integer, primary_key=True)
    personel_id = db.Column(db.String(64), unique=True)
    first_name = db.Column(db.String(64))
    last_name = db.Column(db.String(64))
    national_id = db.Column(db.String(64), unique=True)
    phone_number = db.Column(db.String(64), unique=True)
    address = db.Column(db.Text)
    married = db.Column(db.Boolean)
    age = db.Column(db.Integer)
    income = db.Column(db.Integer)
    gender = db.Column(db.Boolean)

    def __repr__(self):
        return '<Employee %r>' % (self.first_name + self.last_name)

    def to_json(self):
        gender= ['Female', 'Male']
        json_emp = {
            'personel_id':self.personel_id,
            'first_name':self.first_name,
            'last_name':self.last_name,
            'national_id':self.national_id,
            'phone_number':self.phone_number,
            'address':self.address,
            'married':self.married,
            'age':self.age,
            'income':self.income,
            'gender':gender[self.gender]
        }
        return json_emp

class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    users = db.relationship('User', backref='role')

    def __repr__(self):
        return '<Role %r>' % self.name


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    @property
    def password(self):
        raise AttributeError('password is no a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User %r>' % self.username
