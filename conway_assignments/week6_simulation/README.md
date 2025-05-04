# Week 6: Bringing it All Together - Simulation in Pygame

**Goal:** Integrate the Conway's Game of Life simulation logic (neighbor counting, rule application) into the interactive Pygame application. Control the simulation speed and state.

**Task:**

1.  **Integrate `count_neighbors`:** Add the `count_neighbors` method back into your `Cell` class (or ensure it's accessible). Adapt it to work with the current grid structure and state representation (e.g., 0/1 or Enum).
    - Remember to handle boundary conditions correctly.
2.  **Integrate `evolve_grid`:** Create the `evolve_grid` function (similar to Week 3). This function takes the current grid, calculates the next state for every cell based on Conway's rules and neighbor counts, and returns a _new_ grid representing the next generation.
    - **Crucial:** Use `copy.deepcopy()` to create the initial `next_grid` to avoid modifying the original grid while iterating. Make sure you update the `.state` attribute of the cells in the `next_grid`.
3.  **Simulation Control:** In the main game loop, use the `simulation_active` boolean variable (from Week 5) to determine if the simulation should advance.
    - If `simulation_active` is `True`, call `evolve_grid()` to compute the next state and update the main `grid` variable with the result (`grid = evolve_grid(grid)`).
4.  **Control Simulation Speed:**
    - Use `pygame.time.Clock()` to manage the frame rate and simulation speed.
    - Create a clock object before the main loop: `clock = pygame.time.Clock()`.
    - Inside the loop, after drawing and updating the display, call `clock.tick(FPS)` (where `FPS` is your desired frames-per-second, e.g., 10 for 10 generations per second). This limits the loop speed.
    - Alternatively, if you want a fixed pause between generations when the simulation is active, you can use `pygame.time.wait(milliseconds)` inside the `if simulation_active:` block.
5.  **Drawing Updates:** Ensure the grid is fully redrawn (`draw_grid(screen, grid)`) in each iteration of the main loop _after_ potentially evolving the grid, so the latest state is always displayed.
6.  **Refinement:** Clean up the code, ensure interactions (clicking, keyboard presses) work smoothly alongside the simulation.

**`assignment.py`:**

Combine the interaction logic from Week 5 with the simulation logic from Week 3 (adapted for Pygame). Use the `simulation_active` flag and control the speed using `pygame.time.Clock` or `pygame.time.wait`.
