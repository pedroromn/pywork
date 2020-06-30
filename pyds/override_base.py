#! -*- coding: utf-8 -*-
# Overriding base-class method


class Employee(object):

    def __init__(self, first, last):
        self.first_name = first
        self.last_name = last

    def __str__(self):
        return "{}, {}".format(self.first_name, self.last_name)


class HourlyWorker(Employee):

    def __init__(self, first, last, init_hours, init_wage):
        Employee.__init__(self, first, last)
        self.hours = float(init_hours)
        self.wage = float(init_wage)

    def get_pay(self):
        return float(self.hours * self.wage)

    def __str__(self):
        print "HourlyWorler.__str__ is executing"
        return "{} is an hourly worker with pay of {:.2f}".format(
                Employee.__str__(self), self.get_pay())
