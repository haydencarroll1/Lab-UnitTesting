def solve_sudoku(board):
    """
    Solves a Sudoku puzzle using backtracking algorithm.
    Input: List of lists representing 9x9 Sudoku grid (0 represents empty cells)
    Output: Solved board if solution exists, None if no solution exists
    """
    if not is_valid_board(board):
        return None
    
    # Find empty location
    empty = find_empty(board)
    if not empty:
        return board  # Puzzle is solved
        
    row, col = empty
    
    # Try digits 1-9
    for num in range(1, 10):
        # Check if number is safe to place
        if is_safe(board, row, col, num):
            board[row][col] = num
            
            # Recursively try to solve rest of puzzle
            if solve_sudoku(board):
                return board
                
            # If placing number didn't lead to solution, backtrack
            board[row][col] = 0
            
    return None  # No solution exists

def find_empty(board):
    """Find an empty cell in the board (represented by 0)"""
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return (i, j)
    return None

def is_safe(board, row, col, num):
    """Check if it's safe to place number at given position"""
    # Check row
    for x in range(9):
        if board[row][x] == num:
            return False
    
    # Check column
    for x in range(9):
        if board[x][col] == num:
            return False
    
    # Check 3x3 box
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[i + start_row][j + start_col] == num:
                return False
    
    return True

def is_valid_board(board):
    """Check if initial board state is valid"""
    if not isinstance(board, list) or len(board) != 9:
        return False
    
    for row in board:
        if not isinstance(row, list) or len(row) != 9:
            return False
        for num in row:
            if not isinstance(num, int) or num < 0 or num > 9:
                return False
            
    # Check for initial conflicts
    for i in range(9):
        for j in range(9):
            if board[i][j] != 0:
                temp = board[i][j]
                board[i][j] = 0
                if not is_safe(board, i, j, temp):
                    return False
                board[i][j] = temp
                
    return True