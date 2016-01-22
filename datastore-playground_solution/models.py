from google.appengine.ext import ndb

class Department(ndb.Model):
    dept_name = ndb.StringProperty()
    classes = ndb.KeyProperty(repeated = True)

class Class(ndb.Model):
    class_full_name = ndb.StringProperty()
    department = ndb.KeyProperty()
    students_enrolled = ndb.KeyProperty(repeated = True)

class House(ndb.Model):
    house_name = ndb.StringProperty()
    students = ndb.KeyProperty(repeated = True)

class Student(ndb.Model):
    student_name = ndb.StringProperty()
    student_year = ndb.IntegerProperty(choices = [1, 2, 3, 4])
    current_classes = ndb.KeyProperty(repeated = True)
    completed_classes = ndb.KeyProperty(repeated = True)
    house = ndb.KeyProperty()
