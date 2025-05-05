# Week 5 Assignment: Pygame Interaction - Modifying the Grid

import pygame
import random
# import copy # Needed in week 6
pygame.init()

# --- Constants (reuse from Week 4) ---
GRID_WIDTH = 50
GRID_HEIGHT = 30
CELL_SIZE = 20
SEPARATION = 1
SCREEN_WIDTH = GRID_WIDTH * (CELL_SIZE + SEPARATION)
SCREEN_HEIGHT = GRID_HEIGHT * (CELL_SIZE + SEPARATION)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (100, 100, 100)

# --- Cell Class & State (reuse from Week 4) ---
# Using 0 for DEAD, 1 for ALIVE
# class CellState:
#     DEAD = 0
#     ALIVE = 1

class Cell:
    # Optional: Add a class attribute 'map' to store the grid (will implement in Week 6)
    # map = [[None] * GRID_WIDTH for _ in range(GRID_HEIGHT)]
    
    def __init__(self, state, rect):
        self.state = state # 0 or 1
        self.rect = rect
        self.color = BLACK # Add color as an instance variable
        # Update color based on initial state
        if state == 1:
            self.color = WHITE
        
        # Optional: Add x, y coordinates and store in class map (will implement in Week 6)
        # self.x = x
        # self.y = y
        # self.map[x][y] = self

    # --- Add methods needed for Week 6 --- #
    # def count_neighbors(self, grid, row, col):
    #    # ... (logic from Week 3, adapted for 0/1 states)
    #    pass
    
    # Optional: Consider adding __setattr__ method to automatically update color
    # when state changes (will implement in Week 6)
    # def __setattr__(self, name, value):
    #     if name == "state":
    #         # Set color based on new state
    #         pass
    #     super().__setattr__(name, value)

# --- Global Variables ---
grid = [[None] * GRID_WIDTH for _ in range(GRID_HEIGHT)]
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Conway's Game of Life - Week 5")

# --- Helper Functions ---
def create_grid(randomize=True):
    """Creates or resets the grid. If randomize is True, fills with random states."""
    for r in range(GRID_HEIGHT):
        for c in range(GRID_WIDTH):
            x = c * (CELL_SIZE + SEPARATION)
            y = r * (CELL_SIZE + SEPARATION)
            cell_rect = pygame.Rect(x, y, CELL_SIZE, CELL_SIZE)
            initial_state = 0 # Default to dead
            if randomize:
                initial_state = 1 if random.random() > 0.7 else 0

            # If cell exists, update state, else create new
            if grid[r][c]:
                grid[r][c].state = initial_state
                # Update color based on state
                grid[r][c].color = WHITE if initial_state == 1 else BLACK
            else:
                grid[r][c] = Cell(initial_state, cell_rect)

def draw_grid(screen, grid):
    """Draws the entire grid onto the screen."""
    for r in range(GRID_HEIGHT):
        for c in range(GRID_WIDTH):
            cell = grid[r][c]
            # Use the cell's color attribute instead of calculating it
            pygame.draw.rect(screen, cell.color, cell.rect)

# 1e. Flip State Function
def flip_state(cell, screen):
    """Flips the state of a cell and redraws it immediately."""
    cell.state = 1 - cell.state # Toggle between 0 and 1
    # Update color based on new state
    cell.color = WHITE if cell.state == 1 else BLACK
    # Immediate redraw
    pygame.draw.rect(screen, cell.color, cell.rect)
    # Need pygame.display.flip() later in the main loop for this to show

# 1c. Coordinate Conversion
def get_grid_coords(pixel_pos):
    """Converts pixel coordinates (tuple) to grid coordinates (row, col)."""
    pixel_x, pixel_y = pixel_pos
    col = pixel_x // (CELL_SIZE + SEPARATION)
    row = pixel_y // (CELL_SIZE + SEPARATION)
    # Basic bounds check
    if 0 <= row < GRID_HEIGHT and 0 <= col < GRID_WIDTH:
        return row, col
    return None # Click was outside the grid

# --- Initialization ---
create_grid(randomize=True) # Initial random grid

# --- Main Game Loop ---
running = True
simulation_active = False # 2c. Pause/Start state
prev_i, prev_j = -1, -1 # Track previous cell to prevent rapid toggling

while running:
    # --- Event Handling ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # 1. Mouse Input
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1: # Left mouse button
                # 1b. Get mouse position
                mouse_pos = pygame.mouse.get_pos()
                # 1c. Convert to grid coordinates
                grid_coords = get_grid_coords(mouse_pos)
                if grid_coords:
                    # 1d. Identify Cell
                    r, c = grid_coords
                    clicked_cell = grid[r][c]
                    # 1e. Flip State
                    flip_state(clicked_cell, screen)
                    # Update previous cell position
                    prev_i, prev_j = c, r

    # Handle continuous mouse input (dragging)
    if pygame.mouse.get_pressed()[0]:  # Left mouse button held
        pos = pygame.mouse.get_pos()
        i = pos[0] // (CELL_SIZE + SEPARATION)
        j = pos[1] // (CELL_SIZE + SEPARATION)
        # Only toggle if we moved to a different cell
        if (i != prev_i or j != prev_j) and 0 <= j < GRID_HEIGHT and 0 <= i < GRID_WIDTH:
            prev_i, prev_j = i, j
            flip_state(grid[j][i], screen)

    # Handle keyboard events
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        simulation_active = not simulation_active
        print(f"Simulation {'ACTIVE' if simulation_active else 'PAUSED'}")
    elif keys[pygame.K_BACKSPACE]:
        simulation_active = False # Stop simulation when clearing
        for r in range(GRID_HEIGHT):
            for c in range(GRID_WIDTH):
                if grid[r][c].state == 1:  # Only reset living cells
                    grid[r][c].state = 0
                    grid[r][c].color = BLACK
                    pygame.draw.rect(screen, grid[r][c].color, grid[r][c].rect)
        print("Grid cleared.")
    elif keys[pygame.K_r]:
        simulation_active = False # Stop simulation when randomizing
        create_grid(randomize=True)
        print("Grid randomized.")

    # --- Game Logic (Week 6) ---
    # if simulation_active:
        # grid = evolve_grid(grid)
        # Add delay maybe?
        # pygame.time.wait(100) # milliseconds

    # --- Drawing --- (Only redraw full grid if not actively simulating)
    # In week 6, we might only redraw if simulation_active OR if a key was pressed
    screen.fill(GRAY) # Clear screen
    draw_grid(screen, grid) # Draw current state

    # Update the display
    pygame.display.flip()

# --- Cleanup ---
pygame.quit()
print("Pygame window closed.") 