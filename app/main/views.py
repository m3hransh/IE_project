from datetime import datetime
from flask import render_template, session, redirect, url_for, flash
from . import main
from .. import db
from ..models import Employee
from .forms import RegistrationForm
from flask_login import login_required


@main.route('/', methods=['GET', 'POST'])
@login_required
def index():
    return render_template('index.html')

@main.route('/register', methods=['GET', 'POST'])
@login_required
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        employee = Employee(
            personel_id=form.personel_id,
            first_name=form.first_name.data,
            last_name=form.last_name.data,
            national_id=form.national_id.data,
            phone_number=form.phone_number.data,
            address=form.address.data,
            married=form.married.data,
            age=form.age.data,
            income=form.income.data
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
    if form.personel_id.data:
        employee =\
            Employee.query.filter_by(
                personel_id=form.personel_id.data
                ).first()
        if employee and form.validate_on_submit():
            employee.first_name = form.first_name.data
            employee.last_name=form.last_name.data
            employee.national_id=form.national_id.data
            employee.phone_number=form.phone_number.data
            employee.address=form.address.data
            employee.married=form.married.data
            employee.age=form.age.data
            employee.income=form.income.data
            
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