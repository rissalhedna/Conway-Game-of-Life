# Week 1 Assignment: Python Basics & Grid Representation
# Your code goes here

# 1. Define constants for grid size and cell states
WIDTH = 10
HEIGHT = 10

# Cell state representation - we'll use 0 for dead and 1 for alive
# Later this will become a proper Cell class with states
DEAD = 0
ALIVE = 1

# 2. Create a 2D grid (list of lists)
# Initialize an empty grid of the specified size
grid = [[DEAD for _ in range(WIDTH)] for _ in range(HEIGHT)]

# 3. Create a simple pattern in the grid
# Here we're adding a "blinker" pattern (3 cells in a row)
grid[4][3] = ALIVE
grid[4][4] = ALIVE
grid[4][5] = ALIVE

# 4. Print the grid to the console
# We'll use '0' for dead cells and '1' for alive cells
def print_grid(grid):
    """Print the current state of the grid to the console"""
    for row in grid:
        for cell in row:
            if cell == ALIVE:
                print("1", end="")
            else:
                print("0", end="")
        print()  # Print a newline after each row

# Call the print function to display the grid
print("Initial Grid:")
print_grid(grid)

# Note: In Week 2, we'll convert these simple integers to proper Cell objects
# Each cell will have a state and other properties