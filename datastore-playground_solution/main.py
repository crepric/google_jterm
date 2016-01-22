#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import logging
import models
import json
import pprint
from google.appengine.ext import ndb

class GetHandler(webapp2.RequestHandler):
    def get(self):
        # If this is specified, return all the information we have about a
        # Student with that name.
        student_name = self.request.get('student_name')
        if (student_name):
            results = models.Student.query(models.Student.student_name == student_name).fetch()
            for student in results:
                self.response.write("<pre>")
                self.response.write(pprint.pformat(student.to_dict()))
                self.response.write("</pre><br>")
            return

        # Return a` list of all students (and their information) who are taking
        # this class right now.
        # Stretch: add another param to the query to return those who took it
        # instead.`
        class_name = self.request.get('class_name')
        if (class_name):
            result = ndb.Key(models.Class, class_name)
            self.response.write("<pre>")
            self.response.write(pprint.pformat(result.get().to_dict()))
            self.response.write("</pre><br>")
            return

        # Return all students taking at least one class that belongs to this
        # specific department
        dept_code = self.request.get('dept_code')
        if (dept_code):
            all_ba_classes_keys = ndb.Key(models.Department, dept_code).get().classes
            results = models.Student.query(
                            ndb.AND(models.Student.student_year >= 3,
                                    models.Student.current_classes.IN(all_ba_classes_keys)
                                    )
                        ).fetch()
            for student in results:
                self.response.write("<pre>")
                self.response.write(pprint.pformat(student.to_dict()))
                self.response.write("</pre><br>")
            return

        # Return all students that are NOT taking ANY class that belongs to this
        # specific department
        dept_code_not = self.request.get('dept_code_not')
        if (dept_code_not):
            all_ba_classes_keys = ndb.Key(models.Department, dept_code_not).get().classes
            students_to_exclude = models.Student.query(
                                    models.Student.current_classes.IN(all_ba_classes_keys)
                        ).fetch()
            all_students = models.Student.query().fetch()
            results = [student for student in all_students if student not in students_to_exclude]
            for student in results:
                self.response.write("<pre>")
                self.response.write(pprint.pformat(student.to_dict()))
                self.response.write("</pre><br>")
            return

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello world!')

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/get', GetHandler),
], debug=True)
