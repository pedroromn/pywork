# -*- coding: utf-8 -*-
"""
Created on Sat Aug 29 16:09:15 2015

@author: peyo
"""

import turtle
import random


def main():
    tList = []
    head = 0
    numTurtles = 10
    wn = turtle.Screen()
    wn.setup(500, 500)
    for i in range(numTurtles):
        nt = turtle.Turtle()   # Make a new turtle, initialize values
        nt.setheading(head)
        nt.pensize(2)
        nt.color(random.randrange(256), random.randrange(256), random.randrange(256))
        nt.speed(10)
        wn.tracer(30, 0)
        tList.append(nt)       # Add the new turtle to the list
        head = head + 360/numTurtles

    for i in range(100):
        moveTurtles(tList, 15, i)

    w = tList[0]
    w.up()
    w.goto(0, 40)
    w.write("Mi Bebita Hermosa ", True, "center", "40pt Bold")
    w.goto(0, -35)
    w.write("Te Amo", True, "center", "40pt Bold")


def moveTurtles(turtleList, dist, angle):
    for t in turtleList:   # Make every turtle on the list do the same actions.
        t.forward(dist)
        t.right(angle)

        
if __name__ == '__main__':
    main()
        