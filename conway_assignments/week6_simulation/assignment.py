# Week 6 Assignment: Bringing it All Together - Simulation in Pygame

import pygame
import random
import time
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

# --- Cell Class & State --- (Include color property and class map)
class Cell:
    # Static grid storage - shared by all Cell instances
    map = [[None] * GRID_WIDTH for _ in range(GRID_HEIGHT)]
    
    def __init__(self, x, y, rect, state):
        self.color = BLACK # Default color for dead cells
        self.neighbors = 0 # Store neighbor count
        self.x = x
        self.y = y
        self.state = state # 0 or 1
        self.rect = rect
        # Store this cell in the class map
        self.map[x][y] = self
        
    def __setattr__(self, name, value):
        # Automatically update color when state changes
        if name == "state":
            if value == 1: # ALIVE
                self.color = WHITE
            else: # DEAD
                self.color = BLACK
            # Let the normal assignment happen after this
        super().__setattr__(name, value)
        
    # Efficient neighbor counting - uses the class map directly
    def count_neighbors(self):
        neighbors = 0
        # Check all 8 surrounding cells with boundary checks
        if (
            self.x > 0
            and self.y > 0
            and self.map[self.x - 1][self.y - 1].state == 1
        ):
            neighbors += 1
        if self.x > 0 and self.map[self.x - 1][self.y].state == 1:
            neighbors += 1
        if (
            self.x > 0
            and self.y < GRID_WIDTH - 1
            and self.map[self.x - 1][self.y + 1].state == 1
        ):
            neighbors += 1
        if self.y > 0 and self.map[self.x][self.y - 1].state == 1:
            neighbors += 1
        if (
            self.y < GRID_WIDTH - 1
            and self.map[self.x][self.y + 1].state == 1
        ):
            neighbors += 1
        if (
            self.x < GRID_HEIGHT - 1
            and self.y > 0
            and self.map[self.x + 1][self.y - 1].state == 1
        ):
            neighbors += 1
        if (
            self.x < GRID_HEIGHT - 1
            and self.map[self.x + 1][self.y].state == 1
        ):
            neighbors += 1
        if (
            self.x < GRID_HEIGHT - 1
            and self.y < GRID_WIDTH - 1
            and self.map[self.x + 1][self.y + 1].state == 1
        ):
            neighbors += 1

        return neighbors

# --- Global Variables ---
screen = None

# --- Helper Functions ---
def create_grid(randomize=True):
    """Initialize the grid with cells."""
    global screen
    
    # Set up the pygame screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Conway's Game of Life - Week 6")
    
    print("map initialized with size:", len(Cell.map), "x", len(Cell.map[0]))
    for i in range(GRID_WIDTH):
        for j in range(GRID_HEIGHT):
            x = i * (CELL_SIZE + SEPARATION)
            y = j * (CELL_SIZE + SEPARATION)
            cell_rect = pygame.Rect(x, y, CELL_SIZE, CELL_SIZE)
            
            initial_state = 0
            if randomize:
                initial_state = 1 if random.random() > 0.5 else 0
                
            # Always create a new cell - existing cells will be replaced in the map
            cell = Cell(j, i, cell_rect, initial_state)
            pygame.draw.rect(screen, cell.color, cell.rect)
    
    return screen

def reset_map(screen):
    """Reset all cells to dead state."""
    for row in Cell.map:
        for cell in row:
            cell.state = 0  # Set to DEAD
            pygame.draw.rect(screen, cell.color, cell.rect)

def flip_state(screen, cell):
    """Toggle the state of a cell and update its display."""
    cell.state = 1 - cell.state  # Toggle between 0 and 1
    # Draw the cell with its new color
    pygame.draw.rect(screen, cell.color, cell.rect)

def get_grid_coords(pixel_pos):
    """Convert pixel coordinates to grid coordinates."""
    pixel_x, pixel_y = pixel_pos
    col = pixel_x // (CELL_SIZE + SEPARATION)
    row = pixel_y // (CELL_SIZE + SEPARATION)
    if 0 <= row < GRID_HEIGHT and 0 <= col < GRID_WIDTH:
        return row, col
    return None  # Click was outside the grid

# --- Main Game Loop ---
def run_game():
    # Initialize the game
    running = True
    game_of_life = False  # Start with simulation paused
    clock = pygame.time.Clock()
    delta_time = 0.1  # Time between generations when active

    # Create the initial grid
    screen = create_grid(randomize=True)
    
    # Keep track of the previous cell to avoid rapid toggling
    prev_i, prev_j = -1, -1
    
    # Main game loop
    while running:
        # Handle mouse input for cell toggling
        if pygame.mouse.get_pressed()[0]:  # Left mouse button held
            game_of_life = False  # Pause simulation when editing
            pos = pygame.mouse.get_pos()
            i = pos[0] // (CELL_SIZE + SEPARATION)
            j = pos[1] // (CELL_SIZE + SEPARATION)
            
            # Only toggle if we moved to a different cell to prevent rapid toggling
            if i != prev_i or j != prev_j:
                prev_i, prev_j = i, j
                flip_state(screen, Cell.map[j][i])

        # Handle other events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if pygame.key.get_pressed()[pygame.K_BACKSPACE]:
                    game_of_life = False
                    reset_map(screen)
                    print("resetting grid")
                else:
                    game_of_life = not game_of_life
                    print(f"Simulation {'ACTIVE' if game_of_life else 'PAUSED'}")
        
        # Update neighbor counts for all cells before applying rules
        for row in Cell.map:
            for cell in row:
                cell.neighbors = cell.count_neighbors()
        
        # Apply game of life rules if simulation is active
        if game_of_life:
            for row in Cell.map:
                # Check if we should stop simulation (e.g., user clicked)
                if not game_of_life:
                    break
                for cell in row:
                    # Check if user clicked to stop simulation
                    if pygame.mouse.get_pressed()[0]:
                        game_of_life = False
                        break
                        
                    # Apply Conway's Game of Life rules
                    if cell.state == 1 and cell.neighbors < 2:  # Underpopulation
                        flip_state(screen, cell)
                    elif cell.state == 1 and cell.neighbors in [2, 3]:  # Survival
                        pass
                    elif cell.state == 1 and cell.neighbors > 3:  # Overpopulation
                        flip_state(screen, cell)
                    elif cell.state == 0 and cell.neighbors == 3:  # Reproduction
                        flip_state(screen, cell)

            # Control simulation speed
            delta_time = clock.tick(FPS) / 1000.0
            delta_time = max(0.001, min(delta_time, 0.1))
            if game_of_life:
                time.sleep(delta_time)
                
        # Update the display
        pygame.display.flip()

    # Cleanup when done
    pygame.quit()

# Start the game
if __name__ == "__main__":
    run_game() 