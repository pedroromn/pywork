# -*- coding: utf-8 -*-

"""
Date: 20/08/2015
author: peyoromn
"""
"""
Una forma de implementar el cifrado Cesar
"""
plainText = raw_input("Enter a one-word, lowercase message: ")
distance = input("Enter de distance value: ")

code = ""

for ch in plainText:
	ordValue = ord(ch)
	cipherValue = ordValue + distance
	if cipherValue > ord('z'):
		cipherValue = ord('a') + distance - \
						(ord('z') - ordValue + 1)
	code += chr(cipherValue)

print code