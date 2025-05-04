# Week 5: Pygame Interaction - Modifying the Grid

**Goal:** Learn how to handle user input (mouse clicks and keyboard presses) in Pygame to interact with the Game of Life grid before and during the simulation.

**Task:**

1.  **Mouse Input (`MOUSEBUTTONDOWN`):**
    - In the Pygame event loop, check for the `event.type == pygame.MOUSEBUTTONDOWN`.
    - If a mouse button (specifically the left button, `event.button == 1`) is pressed, get the mouse position (`event.pos` or `pygame.mouse.get_pos()`).
    - **Convert Coordinates:** Convert the screen coordinates (pixels) from the mouse position into grid coordinates (row and column indices). You'll need the `CELL_SIZE` and `SEPARATION` constants for this calculation.
    - **Identify Cell:** Find the `Cell` object at the calculated grid coordinates.
    - **Flip State:** Change the state of the clicked cell (dead to alive, or alive to dead). Create a helper function `flip_state(cell)` for this.
    - **Immediate Redraw (Optional but Recommended):** After flipping the state, immediately redraw _just that cell_ on the screen using its stored `Rect` and new color. This provides instant visual feedback without waiting for the next `pygame.display.flip()`.
2.  **Keyboard Input (`KEYDOWN`):**
    - In the event loop, check for `event.type == pygame.KEYDOWN`.
    - Check which key was pressed using `event.key` (e.g., `pygame.K_SPACE`, `pygame.K_RETURN`, `pygame.K_c`, `pygame.K_r`).
    - **Pause/Start:** Implement a way to pause and resume the simulation (which we'll fully integrate in Week 6). Use a boolean variable (e.g., `simulation_active = False` initially). Pressing a key like the Spacebar or Enter could toggle this variable.
    - **Clear Grid:** Add functionality to clear the grid (set all cells to dead) when a specific key (e.g., `pygame.K_c`) is pressed.
    - **Randomize Grid:** Add functionality to re-randomize the grid when a key (e.g., `pygame.K_r`) is pressed.
3.  **Prevent Drawing While Dragging (Optional):** Modify the mouse click handling so that cells are only flipped once per click, not continuously if the mouse button is held down and dragged. You might need to track the previously clicked cell index.

**Note:** We are still not running the full Conway simulation logic in the main loop. This week focuses on setting up the _controls_ to manipulate the grid and toggle the simulation state.

**`assignment.py`:**

Build upon your Week 4 code. Enhance the event loop to handle `MOUSEBUTTONDOWN` and `KEYDOWN` events as described. Add the necessary helper functions (`flip_state`, coordinate conversion, clear, randomize).
