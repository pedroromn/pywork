#! -*- coding: utf-8 -*-

f = open("integers.txt", 'r')
sum = 0

for line in f:
    line = line.strip()
    number = int(line)
    sum += number

print "The sum is {s}".format(s=sum)
