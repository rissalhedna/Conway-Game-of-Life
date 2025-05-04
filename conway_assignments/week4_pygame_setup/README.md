# Week 4: Introduction to Pygame - Visualizing the Grid

**Goal:** Learn the basics of the Pygame library to create a graphical representation of the Game of Life. Focus on setting up a window, drawing shapes (rectangles), handling colors, and creating the main game loop.

**Task:**

1.  **Install Pygame:** Make sure Pygame is installed (`pip install pygame`).
2.  **Import and Initialize:** Import the `pygame` library and initialize it using `pygame.init()`.
3.  **Set up Display:** Create the game window (screen) using `pygame.display.set_mode()`. Calculate the required screen size based on the grid dimensions, the size of each cell, and any separation between cells.
4.  **Define Colors:** Define color constants using RGB tuples (e.g., `WHITE = (255, 255, 255)`, `BLACK = (0, 0, 0)`).
5.  **Grid Drawing:**
    - Adapt your grid creation logic. As you create `Cell` objects, also create a corresponding `pygame.Rect` object for each cell. Store this `Rect` perhaps as an attribute within the `Cell` object (`self.rect`). The `Rect` will define the cell's position and size on the screen.
    - Write a function `draw_grid(screen, grid)` that iterates through your grid of `Cell` objects. For each cell, use `pygame.draw.rect()` to draw its rectangle onto the screen. The color of the rectangle should depend on the cell's state (e.g., white for alive, black for dead).
6.  **Basic Game Loop:** Create the main Pygame loop (`while running:`).
    - **Event Handling:** Inside the loop, include the event handling block (`for event in pygame.event.get():`). For now, just handle the `pygame.QUIT` event to allow the user to close the window gracefully.
    - **Drawing:** Clear the screen each frame (`screen.fill(BACKGROUND_COLOR)` - maybe black or gray).
    - Call your `draw_grid` function.
    - **Update Display:** Update the entire screen to show what you've drawn using `pygame.display.flip()`.
7.  **Quit Pygame:** After the loop ends, uninitialize Pygame using `pygame.quit()`.

**Note:** For this week, we are _not_ yet running the Game of Life simulation rules within the Pygame loop. The focus is just on displaying the _initial_ state of the grid graphically.

**`assignment.py`:**

Start by importing Pygame. Set up the screen, colors, and adapt your grid/cell structure to include `pygame.Rect`. Implement the `draw_grid` function and the basic Pygame loop structure.
