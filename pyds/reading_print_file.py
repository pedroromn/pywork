#! -*- coding: utf-8 -*- 
# Reading and printing a file

import sys

# open file
try:
    file = open("clients.dat", "r")
except IOError:
    print >> sys.stderr, "File could not be opened"
    sys.exit(1)

records = file.readlines() # retrieve list of lines in file

print "Account".ljust(10),
print "Name".ljust(10),
print "Balance".rjust(10)

for record in records:
    field = record.split()
    print field[0].ljust(10),
    print field[1].ljust(10),
    print field[2].rjust(10)

file.close()