# -*- coding: utf-8 -*- 

class Student(object):
    """ Represents a student. """

    def __init__(self, name, number):
        self._name = name
        self._scores = []
        for count in xrange(number):
            self._scores.append(0)

    def get_name(self):
        return self._name

    def set_score(self, i, score):
        self._scores[i - 1] = score

    def get_score(self, i):
        return self._scores[i - 1]

    def get_average(self):
        sum = reduce(lambda x,y : x+y, self._scores)
        return sum / len(self._scores)
    
    def get_high_score(self):
        return max(self._scores)

    def __str__(self):
        return "Name: " + self._name + "\nScores: " + \
                " ".join(map(str, self._scores))