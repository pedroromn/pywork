#! -*- coding: utf-8 -*-

from __future__ import print_function
import random

def roll_dice():
    die1 = random.randrange(1, 7)
    die2 = random.randrange(1, 7)
    work_sum_dies = die1 + die2
    print("Player rolled {:d} + {:d} = {:d}".format(die1, die2, work_sum_dies))
    return work_sum_dies

def main():
    """ main function """
    sum_dies = roll_dice()
    if sum_dies == 7 or sum_dies == 11:
        game_status = "WON"
    elif sum_dies == 2 or sum_dies == 3 or sum_dies == 12:
        game_status = "LOST"
    else:
        game_status = "CONTINUE"
        my_point = sum_dies
        print("Point is {}".format(my_point))

    while game_status == "CONTINUE":
        sum_dies = roll_dice()
        if sum_dies == my_point:
            game_status = "WON"
        elif sum_dies == 7:
            game_status = "LOST"

    if game_status == "WON":
        print("Player wins")
    else:
        print("Player loses")

if __name__ == '__main__':
    main()
