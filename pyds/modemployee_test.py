#! -*- coding: utf-8 -*-

from mod_employee import Employee


def main():
    print "Number of employees before instantation is {}".format(Employee.count)

    #Create two employees objects
    employee1 = Employee("Susan", "Baker")
    employee2 = Employee("Robert", "Jones")
    employee3 = employee1

    print "Number of employees after instantiation is {}".format(Employee.count)
    #print "Employee3: {} {}".format(employee3.get_fname(), employee3.get_lname())

    #explicitly delete employee objects by removing references
    del employee1
    del employee2
    del employee3

    print "Number of employees after deletion is {}".format(Employee.count)


if __name__ == "__main__":
    main() 