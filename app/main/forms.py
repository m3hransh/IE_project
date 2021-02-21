from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length, Email, Regexp, EqualTo
from wtforms import ValidationError
from ..models import Employee


class RegistrationForm(FlaskForm):
    personel_id = StringField('Personel ID', validators=[
        DataRequired(),
        Regexp(r'^\d+$', 0, 'This should be 10 digits')
    ])
    first_name = StringField('First Name', validators=[
        DataRequired(),
        Length(1, 64),
        Regexp(r'^[A-za-z]+$', 0, 'First Name must have only letters')])

    last_name = StringField('Last Name', validators=[
        DataRequired(),
        Length(1, 64),
        Regexp(r'^[A-za-z]+$', 0, 'Last Name must have only letters')])
    national_id = StringField('National ID', validators=[
        DataRequired(),
        Regexp(r'^\d{10}$', 0, 'This should be 10 digits')
    ])
    phone_number = StringField('Phone Number', validators=[
        DataRequired(),
        Length(1, 20),
        Regexp('^\d+$', 0, 'Phone Number should be numbers')])
    address = StringField('Address', validators=[DataRequired()])
    age = StringField('Age', validators=[
        DataRequired(),
        Regexp(r'^\d{1,3}$', 0, Regexp(
            'Age should be valid number'))
    ])
    income = StringField('Income', validators=[
        DataRequired(),
        Regexp('^\d+$')
    ])
    married = BooleanField('Married')
    submit = SubmitField('Submit')

    def validate_national_id(self, field):
        if Employee.query.filter_by(national_id=field.data).first():
            raise ValidationError('National ID is already registered.')
    
    def validate_personel_id(self, field):
        if Employee.query.filter_by(national_id=field.data).first():
            raise ValidationError('Personel ID is already registered.')

    def validate_phone_number(self, field):
        if Employee.query.filter_by(phone_number=field.data).first():
            raise ValidationError('Phone number is already registered.')
