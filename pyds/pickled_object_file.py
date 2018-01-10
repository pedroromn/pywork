#! -*- coding: utf-8 -*- 
# Opening and writing pickled object to file.

import sys
import cPickle

# open file
try:
    file = open("users.dat", "w")   # open file in write mode
except IOError, message:
    print >> sys.stderr, "File could not be open", message
    sys.exit(1)

print "Enter the user name, name and date of birth."
print "Enter end-of-file to end input."

input_list = []

while 1:
    try:
        account_line = raw_input("? ")
    except EOFError:
        break
    else:
        input_list.append( account_line.split() )

cPickle.dump( input_list, file)
file.close()

