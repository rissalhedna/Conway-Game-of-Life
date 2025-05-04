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
    def __init__(self, state, rect):
        self.state = state # 0 or 1
        self.rect = rect

    # --- Add methods needed for Week 6 --- #
    # def count_neighbors(self, grid, row, col):
    #    # ... (logic from Week 3, adapted for 0/1 states)
    #    pass

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
            else:
                grid[r][c] = Cell(initial_state, cell_rect)

def draw_grid(screen, grid):
    """Draws the entire grid onto the screen."""
    for r in range(GRID_HEIGHT):
        for c in range(GRID_WIDTH):
            cell = grid[r][c]
            color = WHITE if cell.state == 1 else BLACK
            pygame.draw.rect(screen, color, cell.rect)

# 1e. Flip State Function
def flip_state(cell, screen):
    """Flips the state of a cell and redraws it immediately."""
    cell.state = 1 - cell.state # Toggle between 0 and 1
    # Immediate redraw
    color = WHITE if cell.state == 1 else BLACK
    pygame.draw.rect(screen, color, cell.rect)
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
                    # Note: Consider the dragging issue mentioned in README

        # 2. Keyboard Input
        if event.type == pygame.KEYDOWN:
            # 2c. Pause/Start Simulation
            if event.key == pygame.K_SPACE or event.key == pygame.K_RETURN:
                simulation_active = not simulation_active
                print(f"Simulation {'ACTIVE' if simulation_active else 'PAUSED'}")
            # 2d. Clear Grid
            elif event.key == pygame.K_c:
                simulation_active = False # Stop simulation when clearing
                create_grid(randomize=False) # Fill with dead cells
                print("Grid cleared.")
            # 2e. Randomize Grid
            elif event.key == pygame.K_r:
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