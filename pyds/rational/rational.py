# -*- coding: utf-8 -*-


class Rational(object):
    """Represents a rational number."""

    def __init__(self, numer, denom):
        self._numer = numer
        self._denom = denom
        self._reduce()

    def get_numerator(self):
        return self._numer

    def get_denominator(self):
        return self._denom

    def __str__(self):
        return str(self._numer) + "/" + str(self._denom)

    def _reduce(self):
        divisor = self._gcd(self._numer, self._denom)
        self._numer = self._numer / divisor
        self._denom = self._denom / divisor

    def _gcd(self, a, b):
        (a, b) = (max(a,b), min(a,b))
        while b > 0:
            (a, b) = (b, a % b)
        return a

    def __add__(self, other):
        new_numer = self._numer * other._denom + \
                    other._numer * self._denom
        new_denom = self._denom * other._denom
        return Rational(new_numer, new_denom)
