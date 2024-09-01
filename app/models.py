from flask_sqlalchemy import  SQLAlchemy
from flask import  url_for

db= SQLAlchemy()

### define any model here


class Student(db.Model):
    __tablename__ = 'students'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    image = db.Column(db.String(100), nullable=True)
    grade = db.Column(db.Integer, nullable=True)


    def __str__(self):
        return f"{self.name}"

    @property
    def image_url(self):
        return url_for('static', filename=f"students/images/{self.image}")

    @property
    def show_url(self):
        return url_for('students.show', id=self.id)

    @property
    def delete_url(self):
        return url_for('students.delete', id=self.id)

