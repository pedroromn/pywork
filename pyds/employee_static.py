#! -*- coding: utf-8 -*- 
# Class Employee with static method - pag 322


class Employee(object):

    number_employees = 0
    max_employee = 10

    @staticmethod
    def is_crowded():
        return Employee.number_employees > Employee.max_employee

    # create static method
    #is_crowded = staticmethod(is_crowded)

    def __init__(self, first, last):
        self.first_name = first
        self.last_name = last
        self.number_employees += 1

    def __del__(self):
        Employee.number_employees -= 1

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)
