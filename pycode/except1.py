# -*- coding: utf-8 -*-

while True:
    try:
        x = int(raw_input('>>> Please enter a number: '))
        if x % 2 == 0:
            print '{num}'.format(num=x)
        else:
            break
    except ValueError as ve:
        print "Valor errado: ", ve
