#!/usr/bin/python3
'''
Island Perimeter
'''


def island_perimeter(grid):
    ''' returns the perimeter of the island '''
    perimeter = 0

    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == 1:
                perimeter += 4

                if r > 0 and grid[r-1][c] == 1:  # top
                    perimeter -= 1
                if r < len(grid) - 1 and grid[r+1][c] == 1:  # bottom
                    perimeter -= 1
                if c > 0 and grid[r][c-1] == 1:  # left
                    perimeter -= 1
                if c < len(grid[0]) - 1 and grid[r][c+1] == 1:  # right
                    perimeter -= 1

    return perimeter
