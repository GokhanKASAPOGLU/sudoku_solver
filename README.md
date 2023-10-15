# Sudoku Solver

This is a Python program that solves Sudoku puzzles using a backtracking algorithm. Simply input the Sudoku puzzle as a 2D array with 0s representing empty cells, and the program will find a solution if one exists.

## Usage

1. Define your Sudoku puzzle by editing the `board` variable in the Python script. Use a 2D list where 0 represents empty cells, and other numbers represent known values.

2. Run the Python script. If a solution exists, it will be printed to the console.

Example Sudoku board:
```python
board = [
    [0, 0, 4, 0, 6, 0, 0, 0, 0],
    [2, 0, 5, 0, 0, 1, 8, 0, 0],
    [0, 0, 0, 8, 0, 0, 0, 0, 3],
    [0, 9, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 7, 0, 0, 6, 0],
    [1, 0, 8, 0, 0, 5, 3, 0, 0],
    [0, 3, 0, 0, 0, 9, 0, 0, 0],
    [0, 4, 0, 0, 0, 0, 2, 0, 0],
    [9, 0, 2, 0, 5, 0, 0, 0, 7]
]
```
