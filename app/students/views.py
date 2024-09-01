from app.models import Student
from flask import render_template

def index():
    students = Student.query.all()
    return render_template("students/index.html", students=students)