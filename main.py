from enum import Enum
from copy import deepcopy
from subprocess import call
import time

# TODO: 1. Add a function to generate grids of different sizes
# 2. Visualize the grid in a more user-friendly way
# 3. Allow the user to interact with the grid before it starts
# 4. Allow a user to set the speed of the simulation
# 5. Allow a user to interact with the grid as it is changing
# 6. Add a function to save/load the grid to/from a file


class CellState(Enum):
    DEAD = " "
    ALIVE = "*" 

map = [
    [None, None, None],
    [None, None, None],
    [None, None, None],
]


class Cell:
    grid = [
        [None, None, None],
        [None, None, None],
        [None, None, None],
    ]

    def __init__(self, x, y, state: CellState):
        self.x = x
        self.y = y
        self.state = state
        self.grid[x][y] = self
        
    def __str__(self):
        return str(self.state.value)    

    def count_neighbors(self):
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


cell1 = Cell(0, 0, CellState.DEAD)
cell2 = Cell(0, 1, CellState.ALIVE)
cell3 = Cell(0, 2, CellState.DEAD)
cell4 = Cell(1, 0, CellState.DEAD)
cell5 = Cell(1, 1, CellState.ALIVE)
cell6 = Cell(1, 2, CellState.DEAD)
cell7 = Cell(2, 0, CellState.DEAD)
cell8 = Cell(2, 1, CellState.ALIVE)
cell9 = Cell(2, 2, CellState.DEAD)

map = deepcopy(Cell.grid)

def print_grid(grid):
    for row in grid:
        for el in row:
            print(el, sep="", end="")
        print()


# Any live cell with fewer than two live neighbours dies, as if by underpopulation.
# Any live cell with two or three live neighbours lives on to the next generation.
# Any live cell with more than three live neighbours dies, as if by overpopulation.
# Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.

def run_conway():
    while True:
        for row in Cell.grid:
            for el in row:
                if el.state == CellState.ALIVE and el.count_neighbors() < 2:
                    el.__setattr__("state", CellState.DEAD)
                elif el.state == CellState.ALIVE and el.count_neighbors() in [2,3]:
                    el.__setattr__("state", CellState.ALIVE)
                elif el.state == CellState.ALIVE and el.count_neighbors() > 3:
                    el.__setattr__("state", CellState.DEAD)
                elif el.state == CellState.DEAD and el.state == CellState.DEAD and el.count_neighbors()==3:
                    el.__setattr__("state", CellState.ALIVE)
        global map
        map = deepcopy(Cell.grid)
        print_grid(map)
        time.sleep(0.1)
        call("clear")

run_conway()