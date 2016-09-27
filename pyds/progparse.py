#! /usr/bin/python
# -*- coding: utf-8 -*-

import argparse


parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('integers', metavar='N', type=int, nargs='+',
                    help='an integer for the acumulator')
parser.add_argument('--sum', dest='acumulate', action='store_const',
                    const=sum, default=max,
                    help='sum the integers (default: find the max)')

args = parser.parse_args()
print(args.acumulate(args.integers))
