import pygame
from main import CellState
from copy import deepcopy
import time
import random
width = 3
height = 2
separation = 1
cell_size = 50
global neighbors
neighbors = [[0]*width for _ in range(height)]
global map
map = [[0]*width for _ in range(height)]
screen_size = (width * (cell_size + separation), height * (cell_size + separation))

screen = pygame.display.set_mode(screen_size)

pygame.init()

clock = pygame.time.Clock()
delta_time = 0.1

def print_grid(grid):
    for row in grid:
        for el in row:
            print(f'{el}', sep="", end="")
        print()
        
def update_neighbors(i, j, value):   
    global map
    global neighbors 
    if (
        i > 0
        and j > 0
    ):
        neighbors[i - 1][j - 1] += value
    if i > 0:
        neighbors[i - 1][j] += value
    if (
        i > 0
        and j < len(neighbors[0]) - 1
    ):
        neighbors[i - 1][j + 1] += value
    if j > 0:
        neighbors[i][j - 1] += value
    if (
        j < len(neighbors[0]) - 1
    ):
        neighbors[i][j + 1] += value
    if (
        i < len(neighbors) - 1
        and j > 0
    ):
        neighbors[i + 1][j - 1] += value
    if (
        i < len(neighbors) - 1
    ):
        neighbors[i + 1][j] += value
    if (
        i < len(neighbors) - 1
        and j < len(neighbors[0]) - 1
    ):
        neighbors[i + 1][j + 1] += value

def flip_state(i, j, reset=False):
    global map
    global neighbors
    if reset:
        map = [[0]*width for _ in range(height)]
        return
    if map[j][i]==1:
        map[j][i]=0
        update_neighbors(j, i, -1)
    else:
        map[j][i] = 1
        update_neighbors(j, i, 1)

def initialize_grid():
    global map
    global neighbors
    for i in range(len(map)):
        for j in range(len(map[0])):
            if random.random()>0.5: flip_state(j, i)

def run_game():
    global map
    global neighbors
    running = True
    game_of_life = False
    initialize_grid()
    prev_i, prev_j = -1, -1
    while running:
        if pygame.mouse.get_pressed()[0]:
            game_of_life = False
            pos = pygame.mouse.get_pos()
            i = pos[0] // (cell_size + separation)
            j = pos[1] // (cell_size + separation)
            if i != prev_i or j != prev_j:
                prev_i, prev_j = i, j
                flip_state(i, j)
                print_grid(map)
        # if pygame.mouse.get_just_released()[0]:
        #     flip_state(i, j)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if pygame.key.get_pressed()[pygame.K_BACKSPACE]:
                    game_of_life = False
                    for i in range(height):
                        for j in range(width):
                            flip_state(i, j, reset=True)
                    print("resetting grid")
                else: game_of_life = not game_of_life

        for i in range(len(map)):
            for j in range(len(map[0])):
                x = j * (cell_size + separation)
                y = i * (cell_size + separation)
                rect = pygame.Rect(x, y, cell_size, cell_size)
                pygame.draw.rect(screen, (255, 255, 255) if map[i][j] == 1 else (0, 0, 0) , rect)

        if game_of_life:
            for i in range(len(map)):
                if not game_of_life:
                    break
                for j in range(len(map[0])):
                    if pygame.mouse.get_pressed()[0]:
                        game_of_life = False
                        break
                    if map[i][j] == 1 and neighbors[i][j] < 2:
                        flip_state(j, i)
                    elif map[i][j] == 1 and neighbors[i][j] in [2,3]:
                        pass
                    elif map[i][j] == 1 and neighbors[i][j] > 3:
                        flip_state(j, i)
                    elif map[i][j] == 0 and neighbors[i][j]==3:
                        flip_state(j, i)

            delta_time = clock.tick(60) / 1000.0
            delta_time = max(0.001, min(delta_time, 0.1))
            if game_of_life:
                time.sleep(1*delta_time)
        pygame.display.flip()

    pygame.quit()

run_game()
