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