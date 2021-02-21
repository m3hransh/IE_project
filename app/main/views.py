from datetime import datetime
from flask import render_template, session, redirect, url_for, flash, request
from . import main
from .. import db
from ..models import Employee
from .forms import RegistrationForm
from flask_login import login_required


@main.route('/', methods=['GET', 'POST'])
@login_required
def index():
    employees = Employee.query.all()
    return render_template('index.html', employees=employees)


@main.route('/register', methods=['GET', 'POST'])
@login_required
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        gender = {'Male':True, 'Female':False}
        employee = Employee(
            personel_id=form.personel_id.data,
            first_name=form.first_name.data,
            last_name=form.last_name.data,
            national_id=form.national_id.data,
            phone_number=form.phone_number.data,
            address=form.address.data,
            married=form.married.data,
            age=form.age.data,
            income=form.income.data,
            gender=gender[form.gender.data]
        )
        db.session.add(employee)
        db.session.commit()
        flash('Employee has added successfuly.')
        return redirect(url_for('main.register'))
    return render_template('register.html', form=form)


@main.route('/edit', methods=['GET', 'POST'])
@login_required
def edit():
    form = RegistrationForm()
    user_id = request.args.get('user_id')
    if user_id and request.method == 'GET':
        emp = Employee.query.filter_by(personel_id=user_id).first()
        if emp:
            form.personel_id.data = emp.personel_id
            form.first_name.data = emp.first_name
            form.last_name.data = emp.last_name
            form.national_id.data = emp.national_id
            form.phone_number.data = emp.phone_number
            form.address.data = emp.address
            form.married.data = emp.married
            form.age.data = emp.age
            form.income.data = emp.income
            form.gender.data = str(emp.gender)
    
    if form.personel_id.data and request.method == 'POST':
        employee =\
            Employee.query.filter_by(
                personel_id=form.personel_id.data
            ).first()
        if employee and form.validate_on_submit():
            gender = {'Male':True, 'Female':False}
            employee.first_name = form.first_name.data
            employee.last_name = form.last_name.data
            employee.national_id = form.national_id.data
            employee.phone_number = form.phone_number.data
            employee.address = form.address.data
            employee.married = form.married.data
            employee.age = form.age.data
            employee.income = form.income.data
            employee.gender = gender[form.gender.data]
            

            db.session.add(employee)
            db.session.commit()
            flash('The employee has edited successfuly.')
            return redirect(url_for('main.edit'))
        else:
            flash("The Personel ID wasn't found")
    return render_template('edit.html', form=form)


@main.route('/remove', methods=['GET', 'POST'])
@login_required
def remove():
    form = RegistrationForm()
    if form.personel_id.data:
        employee =\
            Employee.query.filter_by(
                personel_id=form.personel_id.data
            ).first()
        if employee:
            db.session.delete(employee)
            db.session.commit()
            flash('The employee has removed successfuly.')
            return redirect(url_for('main.remove'))
        else:
            flash("The Personel ID wasn't found")
    return render_template('remove.html', form=form)


@main.route('/stats', methods=['GET', 'POST'])
@login_required
def stats():
    import statistics 
    emps = Employee.query.all()
    stats = {}
    stats['married'] = len([e for e in emps if e.married == True])
    stats['single'] = len(emps) - stats['married']
    stats['million_income'] = len([e for e in emps if e.income > 1000000])
    if len(emps) >0:
        stats['max_income_user'] = max(emps, key=lambda x: x.income)
        stats['min_income_user'] = min(emps, key=lambda x: x.income)
        stats['income_sum'] = sum([e.income for e in emps])
    try:
        stats['stdev'] = statistics.stdev([e.income for e in emps])
    except statistics.StatisticsError:
        stats['stdev'] = 0
    return render_template('stats.html', stats=stats)