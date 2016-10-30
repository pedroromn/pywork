#! -*- coding: utf-8 -*-

"""
Program: textanalysis.py
Computes and displays the Flesch Index and the Grade
Level Equivalent for the readability of a text file
"""

# Take the input
file_name = raw_input("Enter the file name: ")
input_file = open(file_name, 'r')
text = input_file.read()


# Count the sentences
sentences = text.count('.') + text.count('?') + \
            text.count(':') + text.count(';') + \
            text.count('!')

# Count the words
words = len(text.split())

# Count the sylables
sylables = 0
for word in text.split():
    for vowel in ['a', 'e', 'i', 'o', 'u']:
        sylables += word.count(vowel)
    for ending in ['es', 'ed', 'e']:
        if word.endswith(ending):
            sylables -= 1
    if word.endswith('le'):
        sylables += 1


# Compute the Flesch Index and Grade Level
index = 206.835 * (words / float(sentences)) - \
        84.6 * (sylables / words)
level = int(round(0.39 * (words / float(sentences)) + 11.8 * \
                  (sylables / float(words)) - 15.59))


# Output the results
print "The Flesch Index is {fi}".format(fi = index)
print "The Grade Level Equivalent is {gl}".format(gl = level)
print sentences, "sentences"
print words, "words"
print sylables, "syllables"
