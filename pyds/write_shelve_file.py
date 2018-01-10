#! -*- coding: utf-8 -*-
# Writing to shelve file

import sys
import shelve


# open shelve file
try:
    out_credit = shelve.open("credit.dat")
except IOError:
    print >> sys.stder, "File could not be opened"
    sys.exit(1)

print "Enter account number (1 to 100, 0 to end input)"

# get account information
while 1:
    # get account information
    account_number = int(raw_input("\nEnter account number\n? "))

    if 0 < account_number <= 100:
        print "Enter lastname, firstname, balance"
        current_data = raw_input("? ")
        out_credit[ str(account_number) ] = current_data.split()
    elif account_number == 0:
        break

out_credit.close()  # close shelve file