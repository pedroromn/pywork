# -*- coding: utf-8 -*-

from die import Die


class Player(object):

    def __init__(self):
        self._die1 = Die()
        self._die2 = Die()
        self._rolls = []

    def __str__(self):
        result = ""
        for (v1,v2) in self._rolls:
            result = result + str((v1,v2)) + " " + \
                    str(v1 + v2) + "\n"
        return result

    def get_number_rolls(self):
        return len(self._rolls)

    def play(self):
        self._rolls = []
        self._die1.roll()
        self._die2.roll()
        (v1, v2) = (self._die1.get_value(),
                    self._die2.get_value())
        self._rolls.append((v1,v2))
        initial_sum = v1 + v2
        if initial_sum in (2, 3, 12):
            return False
        elif initial_sum in (7, 11):
            return True
        while True:
            self._die1.roll()
            self._die2.roll()
            (v1, v2) = (self._die1.get_value(),
                    self._die2.get_value())
            self._rolls.append((v1,v2))
            sum = v1 + v2
            if sum == 7:
                return False
            elif sum == initial_sum:
                return True

