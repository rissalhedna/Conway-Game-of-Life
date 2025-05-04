# Week 3: Game Logic - Counting Neighbors & Applying Rules

**Goal:** Implement the core rules of Conway's Game of Life. Learn how to access elements in a 2D grid, handle boundary conditions (edges and corners), and update the state of the grid based on rules.

**Task:**

1.  **Count Neighbors Method:** Add a method to your `Cell` class called `count_neighbors`. This method needs access to the _entire grid_ to check the state of the 8 surrounding cells.
    - **Challenge:** How will the `count_neighbors` method know about the grid? You might need to pass the grid as an argument or think about how the `Cell` class can access it (perhaps by making the grid a class variable or passing coordinates).
    - **Boundary Conditions:** Be careful when checking neighbors for cells at the edges or corners of the grid. You need to avoid `IndexError` exceptions.
2.  **Game Rules:** Implement the rules of Conway's Game of Life:
    - Any live cell with fewer than two live neighbours dies (underpopulation).
    - Any live cell with two or three live neighbours lives on to the next generation.
    - Any live cell with more than three live neighbours dies (overpopulation).
    - Any dead cell with exactly three live neighbours becomes a live cell (reproduction).
3.  **Evolve the Grid:** Write a function (e.g., `evolve_grid`) that creates the _next_ state of the grid.
    - **Important:** You cannot modify the grid _in place_ while you are calculating the next state. Why? Because changing a cell's state might affect the neighbor count for adjacent cells that haven't been processed yet.
    - **Solution:** Create a _new_ grid (e.g., `next_grid`) to store the calculated next states. Iterate through the _current_ grid, calculate the next state for each cell based on its neighbors in the _current_ grid, and store that new state in the corresponding position in the `next_grid`.
    - After processing all cells, replace the old grid with the `next_grid`.
4.  **Simulation Loop:** Create a basic loop that prints the current grid, calculates the next grid state, updates the grid, and maybe waits for a short time (using `import time; time.sleep(0.5)`) before repeating. This will show the animation in the terminal.

**`assignment.py`:**

Build upon your Week 2 code. Add the `count_neighbors` method, the `evolve_grid` function, and the main simulation loop.
