#! -*- coding: utf-8 -*-
# newlist.py
# Definition for class SingleList


class SingleList(list):

    # constructor
    def __init__(self, init_list=None):
        list.__init__(self)

        if init_list:
            self.merge(init_list)

    
    # utility method
    def _raise_ifnot_unique(self, value):
        if value in self:
            raise ValueError, \
                    "List already contains value {}".format(value)
    

    # overloaded sequence operation
    def __setitem__(self, subscript, value):
        self._raise_ifnot_unique(value)
        return list.__setitem__(self, subscript, value)


    # overloaded mathematical operation
    def __add__(self, other):
        return SingleList( list.__add__(self, other) )

    def __radd__(self, other):
        return SingleList( list.__add__(other, self) )

    def __iadd__(self, other):
        for value in other:
            self.append(value)
        return self

    def __mul__(self, value):
        raise ValueError, "Cannot repeat values in SingleList"

    # __rmul__ and __imul__  have same behavior as __mul__
    __rmul__ = __imul__ = __mul__

    # overridden list methods
    def insert(self, subscript, value):
        # terminate method on no-unique value
        self._raise_ifnot_unique(value)
        return list.insert(self, subscript, value)

    def append(self, value):
        self._raise_ifnot_unique(value)
        return list.append( list.append(self, value) )

    def extend(self, other):
        for value in other:
            self.append(value)

    # New SingleList method
    def merge(self, other):
        for value in other:
            if value not in self:
                list.append(self, value)