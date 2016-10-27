# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 19:47:20 2015

@author: peyo
"""


def matrix_transpose(m):
    mt = [[row[i] for row in m] for i in range(len(m[0]))]
    return mt 

def main():
    matrix = [[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9, 10, 11, 12]]
              
    mt = matrix_transpose(matrix)
    
    print mt    
    


if __name__ == '__main__':
    main()         