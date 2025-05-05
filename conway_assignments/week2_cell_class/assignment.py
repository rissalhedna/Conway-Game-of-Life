# Week 2 Assignment: Object-Oriented Programming - The Cell Class

# Import Enum for cell states
from enum import Enum

# Define the CellState Enum
class CellState(Enum):
    DEAD = '0'  # Using '0' for dead cells
    ALIVE = '1' # Using '1' for alive cells

# 1. Define the Cell Class
class Cell:
    # 2. Constructor (__init__)
    def __init__(self, state, row=None, col=None):
        # 3. Attributes (store the state and position)
        self.state = state      # The cell's state (ALIVE or DEAD)
        self.row = row          # The cell's row in the grid
        self.col = col          # The cell's column in the grid
        
        # Note: In Week 6, we'll add:
        # self.neighbors = 0    # To store the count of live neighbors
        # self.color = ...      # To store the cell's display color

    # 4. String Representation (__str__)
    def __str__(self):
        # Return the character representation of the state
        return self.state.value
    
    # In Week 3, we'll add:
    # def count_neighbors(self, grid):
    #    # Method to count the number of living neighbors

# --- Grid Setup ---

# Grid dimensions
width = 10
height = 10

# Create a 2D grid to hold Cell objects
grid = [[None] * width for _ in range(height)]

# Initial pattern (e.g., a simple oscillator)
pattern = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]

# 5. Create Cell Objects and Populate the Grid
for r in range(height):
    for c in range(width):
        # Create a Cell object based on the pattern (1=ALIVE, 0=DEAD)
        state = CellState.ALIVE if pattern[r][c] == 1 else CellState.DEAD
        # Create cell and store row/col position for later use
        grid[r][c] = Cell(state, r, c)

# 6. Print Grid Function
def print_grid(grid):
    """Print the current state of the grid to the console"""
    for row in grid:
        for cell in row:
            print(cell, end="")  # The __str__ method is called automatically
        print()  # Newline after each row

# --- Main Execution ---
print("Initial Grid:")
print_grid(grid)

# Note: In Week 3, we'll add the function to evolve the grid over time
# def evolve_grid(grid):
#     # Apply Conway's Game of Life rules to create the next generation
#     pass 