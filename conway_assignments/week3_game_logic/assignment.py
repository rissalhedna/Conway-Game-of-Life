# Week 3 Assignment: Game Logic - Counting Neighbors & Applying Rules

import time
import copy # Needed for deep copying the grid

# --- Reuse or adapt your Cell class from Week 2 ---
from enum import Enum

class CellState(Enum):
    DEAD = '0'
    ALIVE = '1'

class Cell:
    def __init__(self, state, row=None, col=None):
        self.state = state
        # Add row, col attributes for easier access to cell position
        self.row = row
        self.col = col
        # For Week 6, we'll add a neighbors attribute 
        # to avoid recalculating this for each cell
        # self.neighbors = 0

    def __str__(self):
        if isinstance(self.state, CellState):
            return self.state.value
        return self.state

    # 1. Count Neighbors Method
    def count_neighbors(self, grid):
        """Count the number of live neighbors for this cell"""
        live_neighbors = 0
        grid_height = len(grid)
        grid_width = len(grid[0])
        
        # Get the cell's position
        row = self.row
        col = self.col
        
        # Check each of the 8 surrounding cells
        # There are more efficient ways to write this (see below), but this is explicit
        # Top-left diagonal
        if row > 0 and col > 0 and grid[row-1][col-1].state == CellState.ALIVE:
            live_neighbors += 1
        # Top
        if row > 0 and grid[row-1][col].state == CellState.ALIVE:
            live_neighbors += 1
        # Top-right diagonal
        if row > 0 and col < grid_width-1 and grid[row-1][col+1].state == CellState.ALIVE:
            live_neighbors += 1
        # Left
        if col > 0 and grid[row][col-1].state == CellState.ALIVE:
            live_neighbors += 1
        # Right
        if col < grid_width-1 and grid[row][col+1].state == CellState.ALIVE:
            live_neighbors += 1
        # Bottom-left diagonal
        if row < grid_height-1 and col > 0 and grid[row+1][col-1].state == CellState.ALIVE:
            live_neighbors += 1
        # Bottom
        if row < grid_height-1 and grid[row+1][col].state == CellState.ALIVE:
            live_neighbors += 1
        # Bottom-right diagonal
        if row < grid_height-1 and col < grid_width-1 and grid[row+1][col+1].state == CellState.ALIVE:
            live_neighbors += 1

        return live_neighbors

        # More compact way to check neighbors (optional):
        # for i in range(max(0, row - 1), min(grid_height, row + 2)):
        #     for j in range(max(0, col - 1), min(grid_width, col + 2)):
        #         # Skip the cell itself
        #         if i == row and j == col:
        #             continue
        #         # Check if the neighbor is ALIVE
        #         if grid[i][j].state == CellState.ALIVE:
        #             live_neighbors += 1
        # return live_neighbors

# --- Grid Setup ---
width = 10
height = 10
grid = [[None] * width for _ in range(height)]

# Initialize grid with Cell objects (e.g., a glider pattern)
# First, fill with dead cells
for r in range(height):
    for c in range(width):
        grid[r][c] = Cell(CellState.DEAD, r, c)

# Then set a specific pattern (glider):
# ...*..
# .*.*..
# ..**..
# ......
grid[1][3].state = CellState.ALIVE
grid[2][1].state = CellState.ALIVE
grid[2][3].state = CellState.ALIVE 
grid[3][2].state = CellState.ALIVE
grid[3][3].state = CellState.ALIVE

# --- Game Logic ---

def print_grid(grid):
    """Print the grid to the console"""
    for row in grid:
        for cell in row:
            print(cell, end="")
        print()  # New line after each row

# 3. Evolve the Grid Function
def evolve_grid(current_grid):
    """Apply Conway's rules to create the next generation"""
    height = len(current_grid)
    width = len(current_grid[0])
    
    # Step 1: Create a deep copy for the next generation
    # This is necessary to ensure all cells update based on current state
    next_grid = copy.deepcopy(current_grid)
    
    # Note: In Week 6, we'll learn a more efficient approach that eliminates
    # the need for deepcopy by pre-calculating and storing neighbor counts

    # Step 2: Apply rules for each cell
    for r in range(height):
        for c in range(width):
            cell = current_grid[r][c]
            live_neighbors = cell.count_neighbors(current_grid)
            
            # 2. Apply Conway's Rules
            if cell.state == CellState.ALIVE:
                # Rule 1: Any live cell with fewer than two live neighbors dies (underpopulation)
                if live_neighbors < 2:
                    next_grid[r][c].state = CellState.DEAD
                # Rule 2: Any live cell with two or three live neighbors lives on
                elif live_neighbors in [2, 3]:
                    pass  # No change needed - state stays ALIVE
                # Rule 3: Any live cell with more than three live neighbors dies (overpopulation)
                elif live_neighbors > 3:
                    next_grid[r][c].state = CellState.DEAD
            else:  # cell is DEAD
                # Rule 4: Any dead cell with exactly three live neighbors becomes alive (reproduction)
                if live_neighbors == 3:
                    next_grid[r][c].state = CellState.ALIVE

    return next_grid

# --- Simulation Loop ---

# 4. Main Loop
def run_simulation(grid, num_generations=20, delay=0.2):
    """Run the simulation for a specified number of generations"""
    print("Initial State:")
    print_grid(grid)
    
    for generation in range(num_generations):
        # Calculate the next generation
        grid = evolve_grid(grid)
        
        # Display the new state
        print(f"\nGeneration {generation + 1}:")
        print_grid(grid)
        
        # Pause for visibility
        time.sleep(delay)
        
    print("\nSimulation complete!")

# Start the simulation!
if __name__ == "__main__":
    run_simulation(grid) 