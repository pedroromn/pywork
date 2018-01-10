#! -*- coding: utf-8 -*-
# Reading shelve file

import sys
import shelve

# print formatted credit data
def output_line( account, alist ):
    print account.ljust(10),
    print alist[0].ljust(10),
    print alist[1].ljust(10),
    print alist[2].rjust(10)

def main():
    # open shelve file
    try:
        credit_file = shelve.open("credit.dat")
    except IOError:
        print >> sys.stderr, "File could not be opened"
        sys.exit(1)

    print "Account".ljust(10),
    print "Last Name".ljust(10),
    print "First Name".ljust(10),
    print "Balance".rjust(10)

    # display each account
    for account_number in credit_file.keys():
        output_line( account_number, credit_file[ account_number ])

    credit_file.close()

if __name__ == "__main__":
    main()