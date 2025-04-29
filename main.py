import subprocess
import time
from enum import Enum


class CellState(Enum):
    DEAD = " "
    ALIVE = "*"


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
            and str(self.grid[self.x - 1][self.y - 1]) == CellState.ALIVE.value
        ):
            neighbors += 1
        if self.x > 0 and str(self.grid[self.x - 1][self.y]) == CellState.ALIVE.value:
            neighbors += 1
        if (
            self.x > 0
            and self.y < len(self.grid[0]) - 1
            and str(self.grid[self.x - 1][self.y + 1]) == CellState.ALIVE.value
        ):
            neighbors += 1
        if self.y > 0 and str(self.grid[self.x][self.y - 1]) == CellState.ALIVE.value:
            neighbors += 1
        if (
            self.y < len(self.grid[0]) - 1
            and str(self.grid[self.x][self.y + 1]) == CellState.ALIVE.value
        ):
            neighbors += 1
        if (
            self.x < len(self.grid) - 1
            and self.y > 0
            and str(self.grid[self.x + 1][self.y - 1]) == CellState.ALIVE.value
        ):
            neighbors += 1
        if (
            self.x < len(self.grid) - 1
            and str(self.grid[self.x + 1][self.y]) == CellState.ALIVE.value
        ):
            neighbors += 1
        if (
            self.x < len(self.grid) - 1
            and str(self.y < len(self.grid[0]) - 1)
            and str(self.grid[self.x + 1][self.y + 1]) == CellState.ALIVE.value
        ):
            neighbors += 1

        return neighbors


def print_grid(grid):
    for row in grid:
        for el in row:
            print(el.value, sep="")
        print()


cell1 = Cell(0, 0, CellState.DEAD)
cell2 = Cell(0, 1, CellState.ALIVE)
cell3 = Cell(0, 2, CellState.DEAD)
cell4 = Cell(1, 0, CellState.DEAD)
cell5 = Cell(1, 1, CellState.DEAD)
cell6 = Cell(1, 2, CellState.DEAD)
cell7 = Cell(2, 0, CellState.DEAD)
cell8 = Cell(2, 1, CellState.ALIVE)
cell9 = Cell(2, 2, CellState.DEAD)

map = [[cell1, cell2, cell3], [cell4, cell5, cell6], [cell7, cell8, cell9]]


def print_grid(grid):
    for row in grid:
        for el in row:
            print(el, sep="", end="")
        print()


print_grid(Cell.grid)
# Any live cell with fewer than two live neighbours dies, as if by underpopulation.
# Any live cell with two or three live neighbours lives on to the next generation.
# Any live cell with more than three live neighbours dies, as if by overpopulation.
# Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.

while True:
    print_grid(Cell.grid)
    for row in Cell.grid:
        for el in row:
            if el.count_neighbors() < 2:
                print(str(el) + " dies.")

    time.sleep(500)
