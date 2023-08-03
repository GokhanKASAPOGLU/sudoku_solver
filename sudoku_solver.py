def find_empty(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return (i, j)  # Return the row and column indices of the empty cell
    return None  # Return None if there are no empty cells on the board

def is_valid(board, num, pos):
    # Check the row for the same number
    for i in range(9):
        if board[pos[0]][i] == num and pos[1] != i:
            return False

    # Check the column for the same number
    for i in range(9):
        if board[i][pos[1]] == num and pos[0] != i:
            return False

    # Check the 3x3 box for the same number
    box_row = pos[0] // 3
    box_col = pos[1] // 3

    for i in range(box_row * 3, box_row * 3 + 3):
        for j in range(box_col * 3, box_col * 3 + 3):
            if board[i][j] == num and (i, j) != pos:
                return False

    return True

def solve_board(board):
    # Find an empty cell
    empty_pos = find_empty(board)
    if not empty_pos:
        return True
    else:
        row, col = empty_pos

    # Try placing numbers from 1 to 9
    for i in range(1, 10):
        if is_valid(board, i, (row, col)):
            board[row][col] = i
            if solve_board(board):
                return True
            board[row][col] = 0

    return False

def print_board(board):
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - -")
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print("|", end="")
            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")

# Sample Sudoku board (replace the 0s with the initial Sudoku puzzle)
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
#[0, 0, 0, 0, 0, 0, 0, 0, 0],
if solve_board(board):
    print("Sudoku Puzzle Solved:")
    print_board(board)
else:
    print("No solution exists for the given Sudoku puzzle.")
