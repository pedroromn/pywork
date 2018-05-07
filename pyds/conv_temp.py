# -*- coding: utf-8 -*-
# Converting temperatura from Celsius to Farenheit

from __future__ import division


def main():
    C = 21
    F = (9/5)*C + 32
    print "{} ºC -> {} ºF ".format(C, F)

if __name__ == "__main__":
    main()