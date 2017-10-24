#! -*- coding: utf-8 -*-
# Demostrating composition: an object with members objects

from employee import Employee

def main():
    print
    employee = Employee("Bob", "Jones", 7, 24, 1949,
                            3, 12, 1988)
    print
    employee.display()
    print

if __name__ == "__main__":
    main()