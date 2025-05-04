import pygame
from main import CellState
from copy import deepcopy
import time
import random
width = 50
height = 30
size = 20
separation = 1

class Cell:
    grid = []
    def __init__(self, x, y, rect, state: CellState):
        self.neighbors = 0
        self.x = y
        self.y = x
        self.state = state
        self.rect = rect
        self.grid[y][x] = self
        
    def __str__(self):
        return str(self.state.value)

    def __setattr__(self, name, value):
        if name == "state":
            if value == CellState.ALIVE:
                colors[self.x][self.y] = (255, 255, 255)
            else:
                colors[self.x][self.y] = (0, 0, 0)
            
        super().__setattr__(name, value)
        
    def count_neighbors(self):
        global map
        
        neighbors = 0
        if (
            self.x > 0
            and self.y > 0
            and str(map[self.x - 1][self.y - 1]) == CellState.ALIVE.value
        ):
            neighbors += 1
        if self.x > 0 and str(map[self.x - 1][self.y]) == CellState.ALIVE.value:
            neighbors += 1
        if (
            self.x > 0
            and self.y < len(map[0]) - 1
            and str(map[self.x - 1][self.y + 1]) == CellState.ALIVE.value
        ):
            neighbors += 1
        if self.y > 0 and str(map[self.x][self.y - 1]) == CellState.ALIVE.value:
            neighbors += 1
        if (
            self.y < len(map[0]) - 1
            and str(map[self.x][self.y + 1]) == CellState.ALIVE.value
        ):
            neighbors += 1
        if (
            self.x < len(map) - 1
            and self.y > 0
            and str(map[self.x + 1][self.y - 1]) == CellState.ALIVE.value
        ):
            neighbors += 1
        if (
            self.x < len(map) - 1
            and str(map[self.x + 1][self.y]) == CellState.ALIVE.value
        ):
            neighbors += 1
        if (
            self.x < len(map) - 1
            and self.y < len(map[0]) - 1
            and str(map[self.x + 1][self.y + 1]) == CellState.ALIVE.value
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

def flip_state(cell, reset=False):
    global map
    global colors
    if reset:
        cell.state = CellState.DEAD
    else: 
        if cell.state == CellState.ALIVE:
            cell.state = CellState.DEAD
        else:
            cell.state = CellState.ALIVE

    pygame.draw.rect(screen, colors[cell.x][cell.y], map[cell.x][cell.y].rect)
    
def create_grid(width, height, cell_size, separation):
    global map
    global colors
    global screen

    screen_size = (width * (cell_size + separation), height * (cell_size + separation))
    screen = pygame.display.set_mode(screen_size)

    map = [[None] * width for _ in range(height)]
    colors = [[None] * width for _ in range(height)]
    Cell.grid = [[None] * width for _ in range(height)]

    print("local grid initialized with size:", len(Cell.grid), "x", len(Cell.grid[0]))
    print("colors initialized with size:", len(colors), "x", len(colors[0]))
    print("map initialized with size:", len(map), "x", len(map[0]))
    for i in range(width):
        for j in range(height):
            x = i * (cell_size + separation)
            y = j * (cell_size + separation)
            rect = pygame.Rect(x, y, size, size)
            map[j][i] = deepcopy(Cell(i, j, rect, CellState.ALIVE if random.random()>0.5 else CellState.DEAD))
            pygame.draw.rect(screen, colors[j][i], map[j][i].rect)
            
    # print_grid(Cell.grid)

def run_game():
    global map
    global colors
    running = True
    game_of_life = False

    create_grid(width, height, size, separation)
   
    prev_i, prev_j = -1, -1
    while running:
        if pygame.mouse.get_pressed()[0]:
            game_of_life = False
            pos = pygame.mouse.get_pos()
            i = pos[0] // (size + separation)
            j = pos[1] // (size + separation)
            if i != prev_i or j != prev_j:
                prev_i, prev_j = i, j
                flip_state(map[j][i])

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if pygame.key.get_pressed()[pygame.K_BACKSPACE]:
                    game_of_life = False
                    for i in range(height):
                        for j in range(width):
                            flip_state(map[i][j], reset=True)
                    print("resetting grid")
                else: game_of_life = not game_of_life
                
        Cell.grid = deepcopy(map)
        if game_of_life:
            for row in Cell.grid:
                if not game_of_life:
                    break
                for el in row:
                    if pygame.mouse.get_pressed()[0]:
                        game_of_life = False
                        break
                    if el.state == CellState.ALIVE and el.count_neighbors() < 2:
                        flip_state(el)
                    elif el.state == CellState.ALIVE and el.count_neighbors() in [2,3]:
                        pass
                    elif el.state == CellState.ALIVE and el.count_neighbors() > 3:
                        flip_state(el)
                    elif el.state == CellState.DEAD and el.count_neighbors()==3:
                        flip_state(el)

            map = deepcopy(Cell.grid)
            delta_time = clock.tick(60) / 1000.0
            delta_time = max(0.001, min(delta_time, 0.1))
            if game_of_life:
                time.sleep(1*delta_time)
        pygame.display.flip()

    pygame.quit()

# create_grid(3, 2, size, separation)
run_game()
