#! -*- coding: utf-8 -*-

import random

def main():
    frequency1 = 0
    frequency2 = 0
    frequency3 = 0
    frequency4 = 0
    frequency5 = 0
    frequency6 = 0

    for roll in xrange(1, 6001):
        face = random.randrange(1, 7)

        if face == 1:
            frequency1 += 1
        elif face == 2:
            frequency2 += 1
        elif face == 3:
            frequency3 += 1
        elif face == 4:
            frequency4 += 1
        elif face == 5:
            frequency5 += 1
        elif face == 6:
            frequency6 += 1
        else:
            print "should never get here!"

    print "Face     {:13s}".format("Frequency")
    print "   1 {:13d}".format(frequency1)
    print "   2 {:13d}".format(frequency2)
    print "   3 {:13d}".format(frequency3)
    print "   4 {:13d}".format(frequency4)
    print "   5 {:13d}".format(frequency5)
    print "   6 {:13d}".format(frequency6)


if __name__ == '__main__':
    import sys
    sys.exit(int(main() or 0))