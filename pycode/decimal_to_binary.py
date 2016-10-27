# -*- coding: utf-8 -*-

"""
Date: 28/08/2015
author: peyoromn
"""


def decimal_to_binary(decimal):
    bstring = ""
    while decimal > 0:
        remainder = decimal % 2
        decimal = decimal / 2
        bstring = str(remainder) + bstring
    return bstring


def main():
    decimal = input("Enter a decimal integer: ")
    binary = decimal_to_binary(decimal)
    print "The binary representation is: {}".format(binary)

if __name__ == '__main__':
    main()
        