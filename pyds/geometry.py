#! -*- coding: utf-8 -*-
# Derived class inheriting from a base class

import math


class Point(object):

    def __init__(self, x_val=0, y_val=0):
        self.x = x_val
        self.y = y_val

    def __str__(self):
        return "( {}, {} )".format(self.x, self.y)


class Circle(Point):

    def __init__(self, x=0, y=0, radius_val=0.0):
        Point.__init__(self,x,y)
        self.radius = float(radius_val)

    def area(self):
        return math.pi * self.radius**2

    def __str__(self):
        return 