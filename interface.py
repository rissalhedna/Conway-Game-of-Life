import pygame
from main import CellState
from copy import deepcopy
import subprocess
import time


class Cell:
    grid = []
    def __init__(self, x, y, rect, state: CellState):
        self.x = y
        self.y = x
        self.state = state
        self.rect = rect
        self.grid[y][x] = self
        
    def __str__(self):
        return str(self.state.value)

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
separation = 1
size = 50
color = (255, 255, 255)

clock = pygame.time.Clock()
delta_time = 0.1

def print_grid(grid):
    for row in grid:
        for el in row:
            print(el, sep="", end="")
        print()

def flip_state(cell):
    global map
    global colors

    if cell.state == CellState.ALIVE:
        cell.state = CellState.DEAD
        colors[cell.x][cell.y] = (0, 0, 0)
    else:
        cell.state = CellState.ALIVE
        colors[cell.x][cell.y] = (255, 255, 255)

    pygame.draw.rect(screen, colors[cell.x][cell.y], map[cell.x][cell.y])
    
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
            colors[j][i] = (0, 0, 0)
            map[j][i] = deepcopy(Cell(i, j, rect, CellState.DEAD))

    print_grid(Cell.grid)



def run_game():
    global map
    global colors
    width = 3
    height = 3
    game_of_life = False
    create_grid(width, height, size, separation)
    
    running = True
    for i in range(width):
        for j in range(height):
            pygame.draw.rect(screen, colors[j][i], map[j][i])

    while running:
        pos = pygame.mouse.get_pos()
        if pygame.mouse.get_just_released()[0]:
            i = pos[0] // (size + separation)
            j = pos[1] // (size + separation)
            flip_state(map[j][i])
            print_grid(map)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                game_of_life = not game_of_life
        while game_of_life:
            for row in Cell.grid:
                for el in row:
                    if el.state == CellState.ALIVE and el.count_neighbors() < 2:
                        el.__setattr__("state", CellState.DEAD)
                        print(f"coordinates: {el.x}, {el.y} underpopulation")
                    elif el.state == CellState.ALIVE and el.count_neighbors() in [2,3]:
                        el.__setattr__("state", CellState.ALIVE)
                        print(f"coordinates: {el.x}, {el.y} alive")
                    elif el.state == CellState.ALIVE and el.count_neighbors() > 3:
                        el.__setattr__("state", CellState.DEAD)
                        print(f"coordinates: {el.x}, {el.y} overpopulation")
                    elif el.state == CellState.DEAD and el.state == CellState.DEAD and el.count_neighbors()==3:
                        el.__setattr__("state", CellState.ALIVE)
                        print(f"coordinates: {el.x}, {el.y} reproduction")    
            map = deepcopy(Cell.grid)
            print_grid(map)
            time.sleep(0.1)

        delta_time = clock.tick(60) / 1000.0
        delta_time = max(0.001, min(delta_time, 0.1))
        pygame.display.flip()

    pygame.quit()

# create_grid(3, 2, size, separation)
run_game()
