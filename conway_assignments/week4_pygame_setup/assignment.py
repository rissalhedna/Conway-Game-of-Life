# Week 4 Assignment: Introduction to Pygame - Visualizing the Grid

# 1. Install Pygame: If you haven't already, run: pip install pygame

# 2. Import and Initialize Pygame
import pygame
import random # To initialize the grid randomly
pygame.init()

# --- Constants ---
# Grid dimensions
GRID_WIDTH = 50
GRID_HEIGHT = 30
# Cell dimensions
CELL_SIZE = 20
SEPARATION = 1 # Gap between cells
# Screen dimensions (calculated)
SCREEN_WIDTH = GRID_WIDTH * (CELL_SIZE + SEPARATION)
SCREEN_HEIGHT = GRID_HEIGHT * (CELL_SIZE + SEPARATION)

# 4. Define Colors (RGB tuples)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (100, 100, 100) # For grid lines or background

# --- Adapt Cell Class --- (Include state and rect)
# Using 0 for DEAD, 1 for ALIVE

class Cell:
    def __init__(self, state, rect):
        self.state = state # 0 for dead, 1 for alive
        # 5. Store the Pygame Rect object for drawing
        self.rect = rect
        
        # Note for Week 5: We'll add a color attribute here 
        # to store the cell's color instead of calculating it each time

    # We don't need __str__ for Pygame visualization
    # But it could be useful for debugging
    def __str__(self):
        return str(self.state)

# --- Grid Creation --- (Now includes Rect creation)
grid = [[None] * GRID_WIDTH for _ in range(GRID_HEIGHT)]

def create_grid():
    """Initialize the grid with Cell objects"""
    for r in range(GRID_HEIGHT):
        for c in range(GRID_WIDTH):
            # Calculate screen position for the cell
            x = c * (CELL_SIZE + SEPARATION)
            y = r * (CELL_SIZE + SEPARATION)
            # Create the pygame.Rect for this cell
            cell_rect = pygame.Rect(x, y, CELL_SIZE, CELL_SIZE)
            # Decide initial state (e.g., random)
            # Use 70% dead cells, 30% alive cells for a good starting pattern
            initial_state = 1 if random.random() > 0.7 else 0

            # Create the Cell object and store in grid
            grid[r][c] = Cell(initial_state, cell_rect)

# --- Drawing --- (Replaces print_grid)
# 5. Grid Drawing Function
def draw_grid(screen, grid):
    """Draw all cells in the grid"""
    for r in range(GRID_HEIGHT):
        for c in range(GRID_WIDTH):
            cell = grid[r][c]
            # Choose color based on state
            # In Week 5, this will be moved into the Cell class
            color = WHITE if cell.state == 1 else BLACK
            # Draw the cell's rectangle with the appropriate color
            pygame.draw.rect(screen, color, cell.rect)

# --- Pygame Setup ---
# 3. Set up Display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Conway's Game of Life - Week 4")

# --- Main Game Loop ---
create_grid() # Initialize the grid cells

running = True
# 6. Basic Game Loop
while running:
    # 6a. Event Handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 6b. Drawing
    screen.fill(GRAY) # Fill background
    draw_grid(screen, grid) # Draw the cells

    # 6c. Update Display
    pygame.display.flip()
    
    # Set frame rate (optional)
    pygame.time.Clock().tick(60)

# 7. Quit Pygame
pygame.quit()

print("Pygame window closed.") 