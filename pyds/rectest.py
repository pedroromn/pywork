#!/usr/bin/python
# -*- coding: utf-8 -*-

import recursion as rec


def lin_sum_test():
    S = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    n = len(S)
    sum_seq = rec.linear_sum(S, n)
    print "La suma de la lista {} es : {}".format(S, sum_seq)


def main():
    lin_sum_test()

if __name__ == '__main__':
    main()
