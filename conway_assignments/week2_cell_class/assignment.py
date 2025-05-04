# Week 2 Assignment: Object-Oriented Programming - The Cell Class

# Optional: Import Enum if you want to use it for states
# from enum import Enum

# Define your CellState Enum here (optional)
# class CellState(Enum):
#     DEAD = ' '
#     ALIVE = '*'

# 1. Define the Cell Class
class Cell:
    # 2. Constructor (__init__)
    def __init__(self, state): # Add parameters as needed (e.g., row, col)
        # 3. Attributes (store the state)
        self.state = state
        # Add other attributes if needed

    # 4. String Representation (__str__)
    def __str__(self):
        # Return the character representation of the state
        # If using Enum: return self.state.value
        # Otherwise: return self.state
        pass # Replace pass with your return statement

# --- Grid Setup (adapt from Week 1) ---

# Grid dimensions (e.g., 3x3)
width = 3
height = 3

grid = [[None] * width for _ in range(height)]

# Example initial pattern (replace with your own)
initial_pattern = [
    [' ', '*', ' '],
    [' ', '*', ' '],
    [' ', '*', ' '],
]

# 5. Create Cell Objects and Populate the Grid
for r in range(height):
    for c in range(width):
        # Create a Cell object based on the initial_pattern
        # state = initial_pattern[r][c] # Or use CellState Enum if you defined it
        # grid[r][c] = Cell(state)
        pass # Replace pass with your code

# 6. Update Printing Logic
def print_grid(grid):
    for row in grid:
        for cell in row:
            # When you print the cell object, its __str__ method is called
            print(cell, end="")
        print() # Newline after each row

# --- Main Execution ---
print("Initial Grid:")
# print_grid(grid) # Uncomment when ready 