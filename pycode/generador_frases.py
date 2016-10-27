# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 15:48:32 2015

@author: peyo
"""

import random

articles = ("A", "THE")

nouns = ("BOY", "GIRL", "BAT", "BALL")

verbs = ("HIT", "SAW", "LIKED")

prepositions = ("WITH", "BY")


def nounPhrase():
    return random.choice(articles) + " " + random.choice(nouns)


def prepositionalPhrase():
    return random.choice(prepositions) + " " + nounPhrase()


def verbPhrase():
    return random.choice(verbs) + " " + nounPhrase() + " " + \
            prepositionalPhrase()


def sentence():
    return nounPhrase() + " " + verbPhrase()


def main():
    number = input("Enter the number of sentence: ")
    for count in xrange(number):
        print sentence()
        
if __name__ == '__main__':
    main()