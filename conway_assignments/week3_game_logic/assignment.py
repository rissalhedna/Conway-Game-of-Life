# Week 3 Assignment: Game Logic - Counting Neighbors & Applying Rules

import time
import copy # Needed for deep copying the grid

# --- Reuse or adapt your Cell class and CellState Enum from Week 2 ---
# from enum import Enum
# class CellState(Enum):
#     DEAD = ' '
#     ALIVE = '*'

class Cell:
    def __init__(self, state): # Add row, col if needed
        self.state = state
        # Add row, col attributes if you pass them
        # self.row = row
        # self.col = col

    def __str__(self):
        # return self.state.value # If using Enum
        return self.state # If using characters

    # 1. Count Neighbors Method
    def count_neighbors(self, grid, row, col):
        live_neighbors = 0
        grid_height = len(grid)
        grid_width = len(grid[0])

        # Iterate through the 8 possible neighbors
        for i in range(max(0, row - 1), min(grid_height, row + 2)):
            for j in range(max(0, col - 1), min(grid_width, col + 2)):
                # Skip the cell itself
                if i == row and j == col:
                    continue

                # Check if the neighbor is ALIVE
                # Make sure grid[i][j] exists and access its state
                # if grid[i][j].state == CellState.ALIVE: # If using Enum
                # if grid[i][j].state == '*': # If using characters
                #    live_neighbors += 1
                pass # Replace pass with your check

        return live_neighbors

# --- Grid Setup (adapt from Week 2) ---
width = 10
height = 10
grid = [[None] * width for _ in range(height)]

# Initialize grid with Cell objects (e.g., a glider pattern)
# ... (your initialization code here, similar to week 2)
# Example: place a simple glider
# grid[1][2] = Cell('*')
# grid[2][3] = Cell('*')
# grid[3][1] = Cell('*')
# grid[3][2] = Cell('*')
# grid[3][3] = Cell('*')
# # Fill the rest with dead cells
# for r in range(height):
#     for c in range(width):
#         if grid[r][c] is None:
#             grid[r][c] = Cell(' ')


# --- Game Logic ---

def print_grid(grid):
    # (Your print_grid function from Week 2)
    pass

# 3. Evolve the Grid Function
def evolve_grid(current_grid):
    height = len(current_grid)
    width = len(current_grid[0])
    # Create a new grid for the next state (use deepcopy for objects)
    next_grid = copy.deepcopy(current_grid)

    for r in range(height):
        for c in range(width):
            cell = current_grid[r][c]
            live_neighbors = cell.count_neighbors(current_grid, r, c)
            current_state = cell.state # Or cell.state if not using Enum

            # 2. Apply Conway's Rules
            new_state = current_state # Assume it stays the same initially
            # Rule 1 & 3: Overpopulation/Underpopulation
            # if current_state == CellState.ALIVE and (live_neighbors < 2 or live_neighbors > 3):
            #     new_state = CellState.DEAD
            # Rule 4: Reproduction
            # elif current_state == CellState.DEAD and live_neighbors == 3:
            #     new_state = CellState.ALIVE
            # Rule 2 is implicit: if live and 2/3 neighbors, state doesn't change

            next_grid[r][c].state = new_state

    return next_grid

# --- Simulation Loop ---

# Initialize grid here...

# 4. Main Loop
num_generations = 20
for generation in range(num_generations):
    print(f"\n--- Generation {generation + 1} ---")
    # print_grid(grid) # Uncomment when ready
    grid = evolve_grid(grid)
    time.sleep(0.5) # Pause for half a second

print("\nSimulation finished.") 