# -*- coding: utf-8 -*-

"""
Date: 28/08/2015
author: peyoromn
"""
"""
Converts a string of bits to decimal integer
"""


def binary_to_decimal(bstring):
	decimal = 0
	exponent = len(bstring) - 1
	for digit in bstring:
		decimal = decimal + int(digit) * 2 ** exponent
		exponent -= 1
	return decimal

def main():
	bstring = raw_input("Enter a string bits: ")
	decimal = binary_to_decimal(bstring)
	print "The integer value is {}".format(decimal)

if __name__ == '__main__':
	main()