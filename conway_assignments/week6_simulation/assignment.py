# Week 6 Assignment: Bringing it All Together - Simulation in Pygame

import pygame
import random
import copy # Needed for evolve_grid
pygame.init()

# --- Constants --- (Reuse from Week 4/5)
GRID_WIDTH = 50
GRID_HEIGHT = 30
CELL_SIZE = 20
SEPARATION = 1
SCREEN_WIDTH = GRID_WIDTH * (CELL_SIZE + SEPARATION)
SCREEN_HEIGHT = GRID_HEIGHT * (CELL_SIZE + SEPARATION)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (100, 100, 100)
FPS = 10 # Frames (generations) per second

# --- Cell Class & State --- (Include count_neighbors)
# Using 0 for DEAD, 1 for ALIVE
class Cell:
    def __init__(self, state, rect):
        self.state = state # 0 or 1
        self.rect = rect

    # 1. Integrate count_neighbors method
    def count_neighbors(self, grid, row, col):
        live_neighbors = 0
        for i in range(max(0, row - 1), min(GRID_HEIGHT, row + 2)):
            for j in range(max(0, col - 1), min(GRID_WIDTH, col + 2)):
                if i == row and j == col:
                    continue
                # Check state of the neighbor cell (must exist due to bounds check)
                if grid[i][j].state == 1: # Check if ALIVE
                    live_neighbors += 1
        return live_neighbors

# --- Global Variables ---
grid = [[None] * GRID_WIDTH for _ in range(GRID_HEIGHT)]
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Conway's Game of Life - Week 6")
clock = pygame.time.Clock() # 4a. Clock for FPS control

# --- Helper Functions (Reuse from Week 5, Add evolve_grid) ---
def create_grid(randomize=True):
    # (Same as Week 5)
    for r in range(GRID_HEIGHT):
        for c in range(GRID_WIDTH):
            x = c * (CELL_SIZE + SEPARATION)
            y = r * (CELL_SIZE + SEPARATION)
            cell_rect = pygame.Rect(x, y, CELL_SIZE, CELL_SIZE)
            initial_state = 0
            if randomize:
                initial_state = 1 if random.random() > 0.7 else 0
            if grid[r][c]:
                grid[r][c].state = initial_state
                grid[r][c].rect = cell_rect # Ensure rect is updated if grid size changes
            else:
                grid[r][c] = Cell(initial_state, cell_rect)

def draw_grid(screen, grid):
    # (Same as Week 5)
    for r in range(GRID_HEIGHT):
        for c in range(GRID_WIDTH):
            cell = grid[r][c]
            color = WHITE if cell.state == 1 else BLACK
            pygame.draw.rect(screen, color, cell.rect)

def flip_state(cell, screen):
    # (Same as Week 5 - but redraw might be less necessary if full redraw happens)
    cell.state = 1 - cell.state
    # Optional: immediate redraw for responsiveness
    # color = WHITE if cell.state == 1 else BLACK
    # pygame.draw.rect(screen, color, cell.rect)

def get_grid_coords(pixel_pos):
    # (Same as Week 5)
    pixel_x, pixel_y = pixel_pos
    col = pixel_x // (CELL_SIZE + SEPARATION)
    row = pixel_y // (CELL_SIZE + SEPARATION)
    if 0 <= row < GRID_HEIGHT and 0 <= col < GRID_WIDTH:
        return row, col
    return None

# 2. Integrate evolve_grid function
def evolve_grid(current_grid):
    # 2a. Create a deep copy to store the next state
    next_grid = copy.deepcopy(current_grid)

    for r in range(GRID_HEIGHT):
        for c in range(GRID_WIDTH):
            cell = current_grid[r][c]
            live_neighbors = cell.count_neighbors(current_grid, r, c)
            current_state = cell.state

            # Apply Conway's Rules
            new_state = current_state
            if current_state == 1: # ALIVE
                if live_neighbors < 2 or live_neighbors > 3:
                    new_state = 0 # Dies
            else: # DEAD
                if live_neighbors == 3:
                    new_state = 1 # Becomes alive

            # Update the state in the *next* grid
            next_grid[r][c].state = new_state

    return next_grid

# --- Initialization ---
create_grid(randomize=True)

# --- Main Game Loop ---
running = True
simulation_active = False # Start paused

while running:
    # --- Event Handling (Reuse from Week 5) ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Mouse clicks (flips state, pauses simulation)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                mouse_pos = pygame.mouse.get_pos()
                grid_coords = get_grid_coords(mouse_pos)
                if grid_coords:
                    r, c = grid_coords
                    clicked_cell = grid[r][c]
                    flip_state(clicked_cell, screen)
                    simulation_active = False # Pause on click
                    print("Cell clicked, Simulation PAUSED")

        # Keyboard input (controls simulation, reset, randomize)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE or event.key == pygame.K_RETURN:
                simulation_active = not simulation_active
                print(f"Simulation {'ACTIVE' if simulation_active else 'PAUSED'}")
            elif event.key == pygame.K_c:
                simulation_active = False
                create_grid(randomize=False)
                print("Grid cleared, Simulation PAUSED")
            elif event.key == pygame.K_r:
                simulation_active = False
                create_grid(randomize=True)
                print("Grid randomized, Simulation PAUSED")

    # --- Game Logic Step ---
    # 3. Run simulation step if active
    if simulation_active:
        grid = evolve_grid(grid)

    # --- Drawing --- (Always redraw the full grid)
    # 5. Drawing Updates
    screen.fill(GRAY) # Clear screen with background color
    draw_grid(screen, grid) # Draw the current state of all cells

    # --- Update Display ---
    pygame.display.flip()

    # 4b. Control Speed
    clock.tick(FPS) # Limit loop speed

# --- Cleanup ---
pygame.quit()
print("Pygame window closed.") 