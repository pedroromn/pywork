# -*- coding: utf-8 -*-

from random import randint


class Die(object):
    
    def __init__(self):
        """The initial face of the die."""
        self._value = 1

    def roll(self):
        self._value = randint(1, 6)

    def get_value(self):
        return self._value

    def __str__(self):
        return str(self._value)