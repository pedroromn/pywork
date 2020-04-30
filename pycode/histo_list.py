#! -*- coding: utf-8 -*-

import random

def main():
    values = [] # list of values
    #print "Enter 10 integers"

    for i in range(10):
        #new_value = int(raw_input("Enter integer {:d}: ".format((i + 1))))
        values += [random.randrange(1, 21)]
    # create histogram
    print "\nCreating a histogram from values:"
    print "{:s} {:5s} {:5s}".format("Element", "Value", "Histogram")

    for i in range(len(values)):
        print "{:5d} {:7d} {:10s}".format((i+1), values[i], "*" * values[i])


if __name__ == '__main__':
    main()
    