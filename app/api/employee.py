from flask import jsonify
from ..models import Employee
from . import api
from ..import db


@api.route('/myget/<name>')
def myget(name):
    emps = Employee.query.filter_by(first_name=name).all()
    return jsonify({'employees': [e.to_json() for e in emps]})


@api.route('/myupdate/<int:id>/<int:income>', methods=['PUT'])
def myupdate(id, income):
    emp = Employee.query.filter_by(personel_id=str(id)).first()
    if emp:
        emp.income = income
        db.session.add(emp)
        db.session.commit()
        e = Employee.query.filter_by(personel_id=str(id)).first()
        return jsonify(
            {'employee': e.to_json()}
        )


@api.route('/mydel/male', methods=['DELETE'])
def mydel_male():
    emps = Employee.query.filter_by(gender=True).all()
    for emp in emps:
        db.session.delete(emp)
    db.session.commit()

    return jsonify({'deleted_employees': len(emps)})


@api.route('/mydel/female', methods=['DELETE'])
def mydel_female():
    emps = Employee.query.filter_by(gender=False).all()
    for emp in emps:
        db.session.delete(emp)
    db.session.commit()
    return jsonify({'deleted_employees': len(emps)})