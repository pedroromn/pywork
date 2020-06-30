#! -*- coding: utf-8 -*- 
# Main program

from employee_static import Employee


def main():
    answers = ["No", "Yes"]     # responses to is_crowded static method
    employee_list = []          # list of objects of class Employees

    # call static method using class
    print "Employees are crowded?"
    print answers[ Employee.is_crowded() ]

    print "Creating 11 objects of class Employees..."

    #create 11 objects of class Employee
    for i in xrange(11):
        employee_list.append( Employee("John", "Doe" + str(i) ) )

        # call static method using object
        print "Employees are crowded?"
        print answers[ employee_list[i].is_crowded() ]

    print "\nRemoving one employee..."
    del employee_list[0]

    print "Employees are crowded? ", answers[ Employee.is_crowded() ]


if __name__ == "__main__":
    main()
