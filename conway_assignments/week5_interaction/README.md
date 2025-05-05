# Week 5: Pygame Interaction - Modifying the Grid

**Goal:** Learn how to handle user input (mouse clicks and keyboard presses) in Pygame to interact with the Game of Life grid before and during the simulation. Enhance the `Cell` class with color properties to prepare for a more efficient implementation.

**Task:**

1.  **Mouse Input (`MOUSEBUTTONDOWN` and Dragging):**

    - In the Pygame event loop, check for the `event.type == pygame.MOUSEBUTTONDOWN`.
    - If a mouse button (specifically the left button, `event.button == 1`) is pressed, get the mouse position (`event.pos` or `pygame.mouse.get_pos()`).
    - **Convert Coordinates:** Convert the screen coordinates (pixels) from the mouse position into grid coordinates (row and column indices). You'll need the `CELL_SIZE` and `SEPARATION` constants for this calculation.
    - **Identify Cell:** Find the `Cell` object at the calculated grid coordinates.
    - **Flip State:** Change the state of the clicked cell (dead to alive, or alive to dead). Create a helper function `flip_state(cell)` for this.
    - **Immediate Redraw:** After flipping the state, immediately redraw _just that cell_ on the screen using its stored `Rect` and new color. This provides instant visual feedback without waiting for the next `pygame.display.flip()`.
    - **Handle Dragging:** Implement continuous cell toggling when the mouse is held down and dragged across the grid. Use `pygame.mouse.get_pressed()` to detect when the mouse button is held down, and track the previous cell position to avoid rapid toggling of the same cell.

2.  **Keyboard Input:**

    - Check which keys are currently pressed using `pygame.key.get_pressed()`, a more responsive approach than waiting for `KEYDOWN` events.
    - **Pause/Start:** Implement a way to pause and resume the simulation (which we'll fully integrate in Week 6). Use a boolean variable (e.g., `simulation_active = False` initially). Pressing Spacebar could toggle this variable.
    - **Reset Grid:** Add functionality to reset the grid (set all cells to dead) when Backspace is pressed.
    - **Randomize Grid:** Add functionality to re-randomize the grid when a key (e.g., `pygame.K_r`) is pressed.

3.  **Cell Class Enhancements:**
    - **Color Attribute:** Add a `color` attribute to the `Cell` class to store the cell's current color (WHITE for alive, BLACK for dead). Update this whenever the state changes rather than calculating it each time.
    - **Cell Map (Optional Preparation):** Consider adding commented code to prepare for next week's class-based map approach. You might add a class attribute `map` to store all cells and `x`, `y` attributes to each cell. This will be fully implemented in Week 6.
    - **State-Color Coupling (Optional Preparation):** Consider adding comments about using `__setattr__` to automatically update a cell's color when its state changes. This will be implemented in Week 6.

**Note:** We are still not running the full Conway simulation logic in the main loop. This week focuses on setting up the _controls_ to manipulate the grid and toggle the simulation state, while preparing for a more efficient implementation structure next week.

**`assignment.py`:**

Build upon your Week 4 code. Enhance the `Cell` class with the color attribute, add continuous dragging support, implement keyboard controls using `get_pressed()`, and add comments about the class-based approach that will be used in Week 6.
