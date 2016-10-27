# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 18:02:58 2015

@author: peyo
"""

text = raw_input("Enter the text: ")

words = []

for word in text.split():
    words.append(word.upper())
    
dicctionary = {}

for word in words:
    number = dicctionary.get(word, None)
    if number == None:
        dicctionary[word] = 1
    else:
        dicctionary[word] = number + 1

maximum = max(dicctionary.values())

print
 
for key in dicctionary:
    if dicctionary[key] == maximum:
        print "Mode: \"{}\" ".format(key)
        break
    