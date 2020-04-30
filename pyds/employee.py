#! -*- coding: utf-8 -*- 
# Definition of Employee class with composite members.

from date import Date

class Employee(object):

    def __init__(self, fname, lname, birth_month, birth_day,
                    birth_year, hire_month, hire_day, hire_year):

        self.birth_date = Date(birth_month, birth_day, birth_year)
        self.hire_date = Date(hire_month, hire_day, hire_year)

        self.last_name = lname
        self.first_name = fname

        print "Employee constructor: {}, {}".format(self.last_name,
                                                self.first_name)
                                                
    def __del__(self):
        print "Employee object about to be destroyed: {}, {}".format(
            self.last_name, self.first_name)

    def display(self):
        print "{}, {}".format(self.last_name, self.first_name)
        print "Hired: {}".format(self.hire_date.display())
        print "Birth date: {}".format(self.birth_date.display())


