#! -*- coding: utf-8 -*-

f = open("numbers.txt", 'r')
sum = 0

for line in f:
    wordlist = line.split()
    for word in wordlist:
        number = float(word)
        sum += number

print "The sum is {s}".format(s=sum)
