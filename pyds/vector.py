# -*- coding: utf-8 -*-


class Vector:
    """ Represent a vector in a multidimensional space"""

    def __init__(self, d):
        """Create d-dimensional vector of zeros"""
        self._coords = [0] * d

    def get_coords(self):
        return self._coords

    def __len__(self):
        return len(self._coords)

    def __getitem__(self, item):
        return self._coords[item]

    def __setitem__(self, key, value):
        self._coords[key] = value

    def __add__(self, other):
        if len(self) != len(other):
            raise ValueError('dimensions must agree')
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] + other[j]
        return result

    def __eq__(self, other):
        return self._coords == other.get_coords

    def __ne__(self, other):
        return not self == other

    @property
    def __str__(self):
        return '<' + str(self._coords)[1:-1] + '>'
