import numpy
import random
import time
import os

grid_size = 30
grid = [[(0 if random.randint(0,100) > 50 else 1) for _ in range(grid_size)] for _ in range(grid_size)]

def update_grid():
    new_grid = [[0 for _ in range(grid_size)] for _ in range(grid_size)]

    for y in range(grid_size):
        for x in range(grid_size):
            # Count neighbours
            alive_neighbours = 0
            for i in (y-1, y, y+1):
                for j in (x-1, x, x+1):
                    if (not (i == y and j == x)) and 0 <= i < grid_size and 0 <= j < grid_size and grid[i][j] == 1:
                        alive_neighbours += 1

            if alive_neighbours == 3 or (alive_neighbours == 2 and grid[y][x] == 1):
                new_grid[y][x] = 1

    return new_grid

while True:
    os.system('cls')
    for row in grid:
        for i in row:
            print('O' if i == 1 else '-', end='')
        print()
    time.sleep(1)
    grid = update_grid()