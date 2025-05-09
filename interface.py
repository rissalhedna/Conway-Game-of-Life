import pygame
from main import CellState
import time
import random
width = 50
height = 30
size = 20
separation = 1

class Cell:
    map = [[None]*width for _ in range(height)]
    def __init__(self, x, y, rect, state: CellState):
        self.color = (0, 0, 0)
        self.neighbors = 0
        self.x = x
        self.y = y
        self.state = state
        self.rect = rect
        self.map[x][y] = self
        
    def __str__(self):
        return str(self.state.value)

    def __setattr__(self, name, value):
        if name == "state":
            if value == CellState.ALIVE:
                self.color = (255, 255, 255)
            else:
                self.color = (0, 0, 0)
            
        super().__setattr__(name, value)
        
    def count_neighbors(self):
        neighbors = 0
        if (
            self.x > 0
            and self.y > 0
            and str(self.map[self.x - 1][self.y - 1]) == CellState.ALIVE.value
        ):
            neighbors += 1
        if self.x > 0 and str(self.map[self.x - 1][self.y]) == CellState.ALIVE.value:
            neighbors += 1
        if (
            self.x > 0
            and self.y < len(self.map[0]) - 1
            and str(self.map[self.x - 1][self.y + 1]) == CellState.ALIVE.value
        ):
            neighbors += 1
        if self.y > 0 and str(self.map[self.x][self.y - 1]) == CellState.ALIVE.value:
            neighbors += 1
        if (
            self.y < len(self.map[0]) - 1
            and str(self.map[self.x][self.y + 1]) == CellState.ALIVE.value
        ):
            neighbors += 1
        if (
            self.x < len(self.map) - 1
            and self.y > 0
            and str(self.map[self.x + 1][self.y - 1]) == CellState.ALIVE.value
        ):
            neighbors += 1
        if (
            self.x < len(self.map) - 1
            and str(self.map[self.x + 1][self.y]) == CellState.ALIVE.value
        ):
            neighbors += 1
        if (
            self.x < len(self.map) - 1
            and self.y < len(self.map[0]) - 1
            and str(self.map[self.x + 1][self.y + 1]) == CellState.ALIVE.value
        ):
            neighbors += 1

        return neighbors
    
pygame.init()

clock = pygame.time.Clock()
delta_time = 0.1

def print_grid(grid):
    for row in grid:
        for el in row:
            print(f'{el}:{el.count_neighbors()}', sep="", end="")
        print()

def reset_map(screen):
    for row in Cell.map:
        for cell in row:
            cell.state = CellState.DEAD
            pygame.draw.rect(screen, cell.color, cell.rect)

def flip_state(screen, cell, reset=False):
    if reset:
        cell.state = CellState.DEAD
    else: 
        if cell.state == CellState.ALIVE:
            cell.state = CellState.DEAD
        else:
            cell.state = CellState.ALIVE

    pygame.draw.rect(screen, cell.color, cell.rect)
    
def create_grid(width, height, cell_size, separation):
    screen_size = (width * (cell_size + separation), height * (cell_size + separation))
    screen = pygame.display.set_mode(screen_size)

    print("map initialized with size:", len(Cell.map), "x", len(Cell.map[0]))
    for i in range(width):
        for j in range(height):
            x = i * (cell_size + separation)
            y = j * (cell_size + separation)
            rect = pygame.Rect(x, y, size, size)
            cell = Cell(j, i, rect, CellState.ALIVE if random.random()>0.5 else CellState.DEAD)
            pygame.draw.rect(screen, cell.color, cell.rect)
    return screen
            

def run_game():
    running = True
    game_of_life = False

    screen = create_grid(width, height, size, separation)
   
    prev_i, prev_j = -1, -1
    while running:
        if pygame.mouse.get_pressed()[0]:
            game_of_life = False
            pos = pygame.mouse.get_pos()
            i = pos[0] // (size + separation)
            j = pos[1] // (size + separation)
            if i != prev_i or j != prev_j:
                prev_i, prev_j = i, j
                flip_state(screen, Cell.map[j][i])

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if pygame.key.get_pressed()[pygame.K_BACKSPACE]:
                    game_of_life = False
                    reset_map(screen)
                    print("resetting grid")
                else: game_of_life = not game_of_life
        
        for row in Cell.map:
            for el in row:
                el.neighbors = el.count_neighbors()
                
        if game_of_life:
            for row in Cell.map:
                if not game_of_life:
                    break
                for el in row:
                    if pygame.mouse.get_pressed()[0]:
                        game_of_life = False
                        break
                    if el.state == CellState.ALIVE and el.neighbors < 2:
                        flip_state(screen, el)
                    elif el.state == CellState.ALIVE and el.neighbors in [2,3]:
                        pass
                    elif el.state == CellState.ALIVE and el.neighbors > 3:
                        flip_state(screen, el)
                    elif el.state == CellState.DEAD and el.neighbors==3:
                          flip_state(screen, el)

            delta_time = clock.tick(60) / 1000.0
            delta_time = max(0.001, min(delta_time, 0.1))
            if game_of_life:
                time.sleep(1*delta_time)
        pygame.display.flip()

    pygame.quit()

# create_grid(3, 2, size, separation)
if __name__ == "__main__":
    run_game()