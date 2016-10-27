# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 12:05:09 2016

@author: peyo
"""

# Start with an empty list
data = []

num = int(raw_input("Enter an integer (0 to quit): "))

while num != 0:
    data.append(num)
    num = int(raw_input("Enter an integer (0 to quit): "))
    
# Sort the values
data.sort()

# Display the values in order ascending
print "The values, sorted into ascending order, are: "
for num in data:
    print num, 