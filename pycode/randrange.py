#! -*- coding: utf-8 -*-

import random

def main():
    for i in xrange(1, 21): # simulates 20 die rolls
        print "{:5d}".format(random.randrange(1, 7)), 

        if i % 5 == 0:
            print

if __name__ == '__main__':
    import sys
    sys.exit(int(main() or 0))