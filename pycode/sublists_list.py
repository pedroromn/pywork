# -*- coding: utf-8 -*-
"""
Created on Fri Feb 26 18:58:10 2016

@author: peyo
"""

##
# Compute all sublists of a list
#

def all_sublists(data):
    sublists = [[]]
    
    # Generate all sublists of data from length 1 to len(data)
    for length in range(1, len(data) + 1):
        # Generate the sublists starting at each  index
        for i in range(0, len(data) - length +1):
            sublists.append(data[i : i + length])
    
    return sublists
    
def main():
    print "The sublists of [1, 2, 3, 4] are: "
    print all_sublists([1, 2, 3, 4])
    
if __name__ == '__main__':
    main()
    