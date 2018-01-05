#! -*- coding: utf-8 -*-
# Opening and writing to a file.

import sys


# open file
try:
    file = open("clients.dat", "w") # open file in mode write
except IOError, message:
    print >> sys.stderr, "File could not be opened", message
    sys.exit(1)

print "Enter the account, name and balance."
print "Enter end-of-file to end input."

while 1:
    try:
        account_line = raw_input("? ") # get account entry
    except EOFError:
        break
    else:
        print >> file, account_line

file.close()