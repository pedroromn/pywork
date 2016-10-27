# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 19:14:16 2016

@author: peyo
"""

##
# Remove the outliers from a data set.
#


def remove_outliers(data, num_outliers):
    retval = sorted(data)
    
    for i in range(num_outliers):
        retval.pop(0)
        
    return retval
    
    
def main():
    values = []
    s = raw_input("Enter a value (blank line to quit): ")
    while s != "":
        num = float(s)
        values.append(num)
        s = raw_input("Enter a value (blank line to quit): ")
        
    if len(values) < 4:
        print "You didn't enter enough values."
    else:
        print "With the outliers removed: {ro}".format(ro=remove_outliers(values,2))
        print "The original data: ", values
        
if __name__ == '__main__':
    main()      