from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_marshmallow import Marshmallow
import base64
import os
from pathlib import Path
import cv2
import numpy as np
# import face_recognition
from imageio import imread
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.secret_key = "prakharshukla"
UPLOAD_FOLDER = 'static\ImgUploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///attendanceflask.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


db = SQLAlchemy(app)
ma = Marshmallow(app)

# Defining Database Model 
class Students(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    admission_No = db.Column(db.String(10))
    student_name = db.Column(db.String(50))
    uploaded_image_extension = db.Column(db.String(10) , default="")
    image_uploaded = db.Column(db.Boolean, default=False)
    present_status = db.Column(db.Boolean, default=False)
    date = db.Column(db.String(20), default="00:00")
    
    def __init__(self, admission_No, student_name):
        self.admission_No = admission_No
        self.student_name = student_name


class StudentSchema(ma.Schema):
    class Meta:
        fields = ('id', 'admission_No', 'student_name', 'uploaded_image_extension',
                  'image_uploaded', 'present_status', 'date')


student_schema = StudentSchema()
students_schema = StudentSchema(many=True)


# ---Getting Student list Route---
@app.route('/get', methods=['GET'])
def get_student_list():
    all_students = Students.query.all()
    results = students_schema.dump(all_students)
    return jsonify(results)

# ---Adding Student Name and Admission No list Route---
@app.route('/add_student', methods=['POST'])
def add_student():
    admission_No = request.json['admission_No']
    student_name = request.json['student_name']
    student = Students.query.filter_by(admission_No=admission_No).first()
    # If admission no already exists in database
    if student != None:
        res = jsonify({'message' : 'Admission no. already exists.' , 'added':'0'})
        return res
    students = Students(admission_No, student_name)
    db.session.add(students)
    db.session.commit()
    res = jsonify({'message' : 'Student Added Successfully' , 'added':'1'})
    return res


# ---Deleting Student Route---
@app.route('/delete_student/<admission_No>/', methods=['DELETE'])
def delete_student(admission_No):
    student = Students.query.filter_by(admission_No=admission_No).first()
    # Deleting the same from static/ImgUploads folder
    filename = f'static\ImgUploads\{admission_No}{student.uploaded_image_extension}'
    if os.path.exists(filename):
        os.remove(filename)
    db.session.delete(student)
    db.session.commit()
    res = jsonify({'message': 'Deleted Successfully' , 'isSuccess' : 'yes'})
    return res


# ---Adding Student Image Route---
@app.route('/add_student/image_upload/<admission_No>/', methods=['POST'])
def add_student_image(admission_No):
    student = Students.query.filter_by(admission_No=admission_No).first()
    if 'file' not in request.files:
        res = jsonify({'message': 'No file part in the request'})
        res.status_code = 400
        return res
    file = request.files['file']
    if file.filename == '':
        res = jsonify({'message': 'No file part in the request'})
        res.status_code = 400
        return res
    if file and allowed_file(file.filename):
        filename = file.filename
        file_extension = os.path.splitext(filename)[1]
        filename = f'{admission_No}{file_extension}'
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        student.image_uploaded = True
        student.uploaded_image_extension = file_extension
        db.session.commit()
        res = jsonify({'message': 'File successfully uploaded'})
        res.status_code = 200
        return res
    else:
        res = jsonify({'message': 'Allowed file types are png, jpg, jpeg'})
        res.status_code = 400
        return res


if __name__ == "__main__":
    app.run(debug=True)
