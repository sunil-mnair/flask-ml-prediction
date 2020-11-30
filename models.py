from app import db
from datetime import *
from pytz import timezone
uae = timezone('Asia/Dubai')

from flask_login import UserMixin,current_user,login_user,logout_user
from flask_admin import Admin,AdminIndexView
from flask_admin.contrib.sqla import ModelView

from sqlalchemy.sql import expression

class User(UserMixin,db.Model):
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    username = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))


class Enquiry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    enquiry_dt = db.Column(db.DateTime, nullable = False)

    name = db.Column(db.String(100))
    gender = db.Column(db.String(4))
    birth_dt = db.Column(db.DateTime,nullable = True)

    country = db.Column(db.String(100))
    school_id = db.Column(db.Integer,db.ForeignKey('school.id'))
    parent_id = db.Column(db.Integer,db.ForeignKey('parent.id'))

    email = db.Column(db.String,nullable = True)
    phone = db.Column(db.String,nullable = True)

    course_id = db.Column(db.Integer,db.ForeignKey('course.id'))
    source_id = db.Column(db.Integer,db.ForeignKey('source.id'))

    amount = db.Column(db.Float,nullable = False)
    sessions = db.Column(db.Float,nullable = False)

    remarks = db.Column(db.String(200),nullable = True)

    created_dt = db.Column(db.DateTime, nullable = False,
    default = datetime.now(uae))
    modified_dt = db.Column(db.DateTime, nullable = False,
    default = datetime.now(uae))

class Parent(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    
    fathers_name = db.Column(db.String(100),nullable = True)
    fathers_email = db.Column(db.String,nullable = True)
    fathers_phone = db.Column(db.String,nullable = True)

    mothers_name = db.Column(db.String(100),nullable = True)
    mothers_email = db.Column(db.String,nullable = True)
    mothers_phone = db.Column(db.String,nullable = True)


    created_dt = db.Column(db.DateTime, nullable = False,
    default = datetime.now(uae))
    modified_dt = db.Column(db.DateTime, nullable = False,
    default = datetime.now(uae))

class School(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    school = db.Column(db.String(200),nullable = False)
    country = db.Column(db.String())
    city = db.Column(db.String())


class Source(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    source = db.Column(db.String(),nullable = False)

class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    category = db.Column(db.String(100),nullable = False)
    course = db.Column(db.String(100),nullable = False)
    amount = db.Column(db.Integer,nullable = False)
    sessions = db.Column(db.Integer,nullable = False)

    # enquiries = db.relationship("EnquiredService",backref='service_master')
    # sales = db.relationship("SoldService",backref='service_master')
    # appointment = db.relationship("AppointmentService",backref='service_master')

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    gender = db.Column(db.String(4))
    birth_dt = db.Column(db.DateTime,nullable = True)

    country = db.Column(db.String(100))
    school_id = db.Column(db.Integer,db.ForeignKey('school.id'))
    parent_id = db.Column(db.Integer,db.ForeignKey('parent.id'))

    email = db.Column(db.String,nullable = True)
    phone = db.Column(db.String,nullable = True)

    source_id = db.Column(db.Integer,db.ForeignKey('source.id'))
    remarks = db.Column(db.String(200),nullable = True)

    created_dt = db.Column(db.DateTime, nullable = False,
    default = datetime.now(uae))
    modified_dt = db.Column(db.DateTime, nullable = False,
    default = datetime.now(uae))

class Enrollment(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    student_id = db.Column(db.Integer,db.ForeignKey('student.id'),nullable=False)
    
    enrollment_date = db.Column(db.DateTime,nullable = False)
    pipeline_date = db.Column(db.DateTime,nullable = True)

    course_id = db.Column(db.Integer,db.ForeignKey('course.id'))
    amount = db.Column(db.Float,nullable = False)
    sessions = db.Column(db.Float,nullable = False)

    start_date = db.Column(db.DateTime,nullable = True)
    paid = db.Column(db.Boolean, server_default=expression.false(),default=False,nullable=False)

    installment = db.Column(db.Boolean, server_default=expression.false(),default=False,nullable=False)
    
    created_dt = db.Column(db.DateTime, nullable = False,
    default = datetime.now(uae))
    modified_dt = db.Column(db.DateTime, nullable = False,
    default = datetime.now(uae))

class Renewal(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    student_id = db.Column(db.Integer,db.ForeignKey('student.id'),nullable=False)
    
    course_id = db.Column(db.Integer,db.ForeignKey('course.id'))
    amount = db.Column(db.Float,nullable = False)
    sessions = db.Column(db.Float,nullable = False)

    created_dt = db.Column(db.DateTime, nullable = False,
    default = datetime.now(uae))
    modified_dt = db.Column(db.DateTime, nullable = False,
    default = datetime.now(uae))

class Installment(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    enrollment_id = db.Column(db.Integer,db.ForeignKey('enrollment.id'),nullable=False)

    payment_date = db.Column(db.DateTime,nullable = False)
    amount = db.Column(db.Float,nullable = False)

    payment_type = db.Column(db.String,nullable = False)

    created_dt = db.Column(db.DateTime, nullable = False,
    default = datetime.now(uae))
    modified_dt = db.Column(db.DateTime, nullable = False,
    default = datetime.now(uae))
 




class AllModelView(ModelView):

    can_delete = False
    page_size = 50
    # can_create = False
    # can_edit = False
    # can_delete = False
    # column_searchable_list = ['name', 'email']
    # column_filters = ['country']
    # column_editable_list = ['name', 'last_name'] # for inline editing
    def is_accessible(self):
        return current_user.is_authenticated
    
    def inaccessible_callback(self,name,**kwargs):
        return redirect(url_for('login'),next=request.url)

class MainAdminIndexView(AdminIndexView):
    def is_accessible(self):
        return current_user.is_authenticated
    
    def inaccessible_callback(self,name,**kwargs):
        return redirect(url_for('login'),next=request.url)