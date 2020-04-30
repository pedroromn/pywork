# -*- coding: utf-8 -*-

"""
enumerate
"""
alist = ['a1', 'a2', 'a3']

for i, a in enumerate(alist):
    print i, a

"""
zip
"""

blist = ['b1', 'b2', 'b3']

for a, b in zip(alist, blist):
    print a, b

"""
enumerate con zip
"""

for i, (a, b) in enumerate(zip(alist, blist)):
    print i, a, b
