# -*- coding: utf-8 -*-

"""
Date: 20/08/2015
author: peyoromn
"""
code = raw_input("Enter the coded text: ")
distance = input("Enter the distance value: ")
plainText = ''
for ch in code:
	ordValue = ord(ch)
	cipherValue = ordValue - distance
	if cipherValue < ord('a'):
		cipherValue = ord('z') - \
						(distance - (ord('a') - ordValue + 1))
	plainText += chr(cipherValue)
print plainText