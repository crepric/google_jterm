import webapp2
from models import Department
from models import House
from models import Class
from models import Student
import random
from google.appengine.ext import ndb

from google.appengine.api import users

class CreateEntriesHandler(webapp2.RequestHandler):
    def get(self):

        # CLEAR All
        query = Department.query()
        entries =query.fetch()
        entry_keys =[entry.key for entry in entries]
        ndb.delete_multi(entry_keys)

        query = House.query()
        entries =query.fetch()
        entry_keys =[entry.key for entry in entries]
        ndb.delete_multi(entry_keys)

        query = Class.query()
        entries =query.fetch()
        entry_keys =[entry.key for entry in entries]
        ndb.delete_multi(entry_keys)

        query = Student.query()
        entries =query.fetch()
        entry_keys =[entry.key for entry in entries]
        ndb.delete_multi(entry_keys)

        user = users.get_current_user()
        if user and users.is_current_user_admin():
            # Create houses
            houses = ['Gryffindor', 'Hufflepuff', 'Ravenclaw', 'Slytherin']
            for house in houses:
                House(house_name=house).put()

            # Create departments
            deps = [
                {'code': 'CS', 'name': 'Computer Science'},
                {'code': 'BA', 'name': 'Business Administration'},
                {'code': 'PHY', 'name': 'Physics'},
                {'code': 'MAT', 'name': 'Mathematics'},
                {'code': 'DRA', 'name': 'Drama'},
                {'code': 'ECE', 'name': 'Electrical Engineering'},
            ]
            for dep in deps:
                Department(id = dep['code'], dept_name = dep['name']).put()

            # Create 40 classes for department, update depts
            classes_count = 40
            for dept in deps:
                department_key = ndb.Key('Department', dept['code'])
                department_obj = department_key.get()
                for i in range(classes_count):
                    class_full_name = "%s - Class %d" % (dept['name'] ,i)
                    class_key = Class(id='%s-%d'%(dept['code'], i),
                          class_full_name = class_full_name,
                        department = department_key).put()
                    department_obj.classes.append(class_key)
                department_obj.put()

            # Create students
            students_count = 1000
            random.seed()
            all_classes = Class.query().fetch()
            all_houses = House.query().fetch()
            for i in range(students_count):
                house = random.choice(all_houses)
                house_key = house.key
                student_name = 'Student %d'% i
                student_year = random.randint(1,4)
                current_classes = random.sample(all_classes, 5)
                current_classes_keys = [el.key for el in current_classes]
                all_classes_keys = [el.key for el in all_classes]
                leftovers = set(all_classes_keys) - set(current_classes_keys)
                completed_classes_keys = random.sample(leftovers, 6*(student_year-1))
                student_key = Student(
                    student_name = student_name,
                    student_year = student_year,
                    current_classes = current_classes_keys,
                    completed_classes = completed_classes_keys,
                    house = house_key).put()
                house.students.append(student_key)
                for el in current_classes:
                    el.students_enrolled.append(student_key)
            # save new status of houses and current classes
            for house in all_houses:
                house.put()
            for current_class in all_classes:
                current_class.put()

        elif user and not users.is_current_user_admin():
            self.redirect(users.create_logout_url('/create_entries'))
        else:
            self.redirect(users.create_login_url('/create_entries'))


app = webapp2.WSGIApplication([
    ('/create_entries', CreateEntriesHandler),
], debug=True)
