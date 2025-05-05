# Week 1: Python Basics & Grid Representation

**Goal:** Learn basic Python syntax, including variables, constants, lists (specifically nested lists), loops (`for`), functions, and printing to the console. Understand how to represent a 2D grid structure in Python for Conway's Game of Life.

**Task:**

1.  **Define Constants:** Create constants for grid dimensions (WIDTH, HEIGHT) and cell states (ALIVE, DEAD) using descriptive variable names. We'll use integers (0 for dead, 1 for alive) as they will work well with our future pygame implementation.

2.  **Represent the Grid:** Create a Python list of lists (a 2D array) to represent the Game of Life grid. Initialize it as a grid of the specified width and height, with all cells initially dead.

3.  **Initialize with a Pattern:** Set specific cells to "alive" to create a recognizable pattern. A simple "blinker" pattern (3 cells in a row) works well for testing.

4.  **Create a Print Function:** Write a function to display the grid in the console. Use a nested loop to iterate through the grid and print appropriate characters for each cell state ('0' for dead, '1' for alive).

5.  **Run and Test:** Execute your code to see the grid printed to the console. Verify that your pattern appears correctly.

**Example Expected Output (for a blinker pattern in a 10x10 grid):**

```
0000000000
0000000000
0000000000
0000000000
0001110000
0000000000
0000000000
0000000000
0000000000
0000000000
```

**`assignment.py`:**

The starter file includes comments outlining the steps above. Fill in the code for each section, implementing the grid representation, pattern initialization, and printing logic.

**Note:** In week 2, we'll convert this simple numeric representation to a more robust object-oriented approach using a proper `Cell` class.
