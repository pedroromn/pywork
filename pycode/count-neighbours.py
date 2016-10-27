# -*- coding: utf-8 -*-

"""
Input: Three arguments. A grid as a tuple of tuples with integers (1/0), 
a row number and column number for a cell as integers.

Output: How many neighbouring cells have chips as an integer.

Example:

count_neighbours(((1, 0, 0, 1, 0),
                  (0, 1, 0, 0, 0),
                  (0, 0, 1, 0, 1),
                  (1, 0, 0, 0, 0),
                  (0, 0, 1, 0, 0),), 1, 2) == 3
count_neighbours(((1, 0, 0, 1, 0),
                  (0, 1, 0, 0, 0),
                  (0, 0, 1, 0, 1),
                  (1, 0, 0, 0, 0),
                  (0, 0, 1, 0, 0),), 0, 0) == 1

Precondition:
3 ≤ len(grid) ≤ 10
all(len(grid[0]) == len(row) for row in grid)

"""

def count_neighbours(grid, row, col):

    # if all(len(grid[0]) == len(row) for row in grid):
    #     for row in grid:
    #         print row
    #     print len(grid), len(grid[0])
    # else:
    #     print "break"

    #  NumeroTotalColumnas => len(grid[0]) -> N
    #  NumeroTotalFilas => len(grid) -> M

    if all(len(grid[0]) == len(rows) for rows in grid):
        neighbours = 0
        M = len(grid)
        N = len(grid[0])
        if row == 0 and col == 0:
            neighbours = grid[row][col + 1] + grid[row + 1][col] + grid[row + 1][col + 1]
        if row == 0 and col == N - 1:
            neighbours = grid[row][col - 1] + grid[row + 1][col] + grid[row + 1][col - 1]
        if row == M - 1 and col == 0:
            neighbours = grid[row - 1][col] + grid[row][col + 1] + grid[row - 1][col + 1]
        if row == M - 1 and col == N - 1:
            neighbours = grid[row][col - 1] + grid[row - 1][col] + grid[row - 1][col - 1]
        if row == 0 and col in range(1, N-1):
            neighbours = grid[row + 1][col - 1] + grid[row + 1][col] + grid[row + 1][col + 1] + grid[row][col - 1] + grid[row][col + 1]
        if row in range(1, M-1) and col == 0:
            neighbours = grid[row - 1][col] + grid[row - 1][col + 1] + grid[row][col + 1] + grid[row + 1][col + 1] + grid[row + 1][col]
        if row == M - 1 and col in range(1, N-1):
            neighbours = grid[row][col - 1] + grid[row - 1][col - 1] + grid[row - 1][col] + grid[row - 1][col+1] + grid[row][col + 1]
        if row in range(1, M-1) and col == N - 1:
            neighbours = grid[row - 1][col] + grid[row - 1][col - 1] + grid[row][col - 1] + grid[row + 1][col - 1] + grid[row + 1][col]
        if row in range(1, M-1) and col in range(1, N-1):
            neighbours = grid[row][col - 1] + grid[row][col + 1] + grid[row - 1][col] + grid[row + 1][col] + grid[row - 1][col - 1] + grid[row - 1][col + 1] + grid[row + 1][col - 1] + grid[row + 1][col + 1]

        return neighbours      



def main():

    grid = ((1,0,0,0,1,0,0,1,1,0),
     (0,1,0,1,0,1,1,0,0,1),
     (1,1,1,1,0,1,0,0,0,1),
     (0,0,1,1,0,1,0,0,0,1),
     (1,1,0,1,1,0,1,0,0,1),
     (0,1,1,1,0,0,1,1,1,0),
     (1,1,1,0,0,0,0,0,1,1),
     (0,0,0,1,0,1,0,0,1,1),
     (0,0,0,1,0,1,0,1,0,1),
     (1,1,0,0,0,1,0,1,1,1),)

    print count_neighbours(grid, 9, 8)
                              


if __name__ == '__main__':
    main()
