#! -*- coding: utf-8 -*- 
# Class Employee with class attribute count.


class Employee(object):

    count = 0   # class attribute (static)

    def __init__(self, fname, lname):
        self.set_name_employee(fname, lname)
        Employee.count += 1     # increment class attribute

    def set_name_employee(self, fname, lname):
        self.set_fname(fname)
        self.set_lname(lname)

    def set_fname(self, fname):
        self.__fname = fname

    def set_lname(self, lname):
        self.__lname = lname

    def get_fname(self):
        return self.__fname

    def get_lname(self):
        return self.__lname

    def __del__(self):
        Employee.count -= 1
        print "Employee destructor for:  {} {}".format(
            self.__lname, self.__fname)

    