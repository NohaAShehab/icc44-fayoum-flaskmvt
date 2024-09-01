from crypt import methods

from app.models import Student, db
from flask import render_template, request, redirect, url_for
from app.students import  student_blueprint

# use blueprint

@student_blueprint.route("", endpoint="index") # generated url /students
def index():
    students = Student.query.all()
    return render_template("students/index.html", students=students)


@student_blueprint.route("<int:id>", endpoint="show")
def show(id):
    student = db.get_or_404(Student, id)
    return  render_template("students/show.html", student=student)


@student_blueprint.route("create", endpoint="create", methods=["GET", "POST"])
def create():
    if request.method == "POST":
        student = Student(name=request.form["name"], grade=request.form["grade"], image=request.form["image"])
        db.session.add(student)
        db.session.commit()
        # return redirect(url_for("students.index"))
        return redirect(student.show_url)


    return render_template("students/create.html")



@student_blueprint.route("<int:id>/delete", endpoint="delete", methods=['POST'])
def delete(id):
    student = db.get_or_404(Student, id)
    db.session.delete(student)
    db.session.commit()
    return redirect(url_for("students.index"))


# add route for edit --> complete the logic

