# Week 2: Object-Oriented Programming - The Cell Class

**Goal:** Introduce Object-Oriented Programming (OOP) concepts in Python. Learn how to define a class, create instances (objects), use the `__init__` constructor, and define methods (functions within a class), including the special `__str__` method.

**Task:**

1.  **Define the `Cell` Class:** Create a Python class named `Cell`.
2.  **Constructor (`__init__`):** Give the `Cell` class an `__init__` method. This method should run when you create a new `Cell` object. It should take parameters for the cell's initial state (alive or dead) and potentially its position (row and column, although we might not use position heavily this week).
3.  **Attributes:** Inside `__init__`, store the cell's state as an attribute (e.g., `self.state`).
4.  **String Representation (`__str__`):** Implement the `__str__` method for the `Cell` class. This method should return the string representation of the cell's state (e.g., `'*'` or `' '`) so that when you `print()` a `Cell` object, it shows its visual state.
5.  **Create Cell Objects:** Modify your grid representation from Week 1. Instead of storing characters directly, store `Cell` objects in the nested list.
6.  **Update Printing:** Adjust your grid printing logic. Since the grid now contains `Cell` objects, printing the grid should automatically use the `__str__` method you defined for each cell.

**Optional Enhancement (Enum):**

- Consider using Python's `Enum` type to define `CellState.ALIVE` and `CellState.DEAD` instead of raw strings. This makes the code more readable and less prone to typos.

**`assignment.py`:**

Start by defining the `Cell` class. Then, adapt your Week 1 grid initialization and printing code to use `Cell` objects.
