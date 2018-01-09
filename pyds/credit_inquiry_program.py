#! -*- coding: utf-8 -*-
# Credit inquiry program

import sys

# retrieve one user command
def get_request():

    while 1:
        request = int(raw_input("\n?"))
        if 1 <= request <= 4:
            break
        else:   # getRequest should never let program reach here
             print "\nInvalid request."
    return request

# determine if balance should be displayed, based on type
def should_display( account_type, balance ):

    if account_type == 2 and balance < 0:   # credit balance
        return 1
    elif account_type == 3 and balance > 0: # debit balance
        return 1
    elif account_type == 1 and balance == 0: # zero balance
        return 1
    else:
        return 0

# print formatted balance data
def output_line( account, name, balance ):

    print account.ljust(10),
    print name.ljust(10),
    print balance.rjust(10)


def main():
    # open file
    try:
        file = open("clients.dat", "r")
    except IOError:
        print >> sys.stderr, "File could not be opened"
        sys.exit(1)

    print "Enter request"
    print "1 - List accounts with zero balance"
    print "2 - List accounts with credit balances"
    print "3 - List accounts with debit balances"
    print "4 - End of run"

    # process user request (s)
    while 1:
        request = get_request() # get user request
        if request == 1: # zero balances
            print "\nAccounts with zero balances:"
        elif request == 2: # credit balances
            print "\nAccounts with credit balances:"
        elif request == 3: # debit balances
            print "\nAccounts with debit balances:"
        elif request == 4: # exit loop
            break
        else:   # getRequest should never let program reach here
             print "\nInvalid request."

        current_record = file.readline()    # get first record

        # process each line
        while( current_record != "" ):
            account, name, balance = current_record.split()
            balance = float(balance)

            if should_display(request, balance):
                output_line( account, name, str(balance) )
            
            current_record = file.readline() # get next line

        file.seek(0, 0)

    print "\nEnd of run."
    file.close()    # close file

if __name__ == "__main__":
    main()
