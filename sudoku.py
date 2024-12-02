def solve_sudoku(board):
    """
    Solves a Sudoku puzzle using backtracking with optimization.
    Input: List of lists representing 9x9 Sudoku grid (0 represents empty cells)
    Output: Returns a new completed board if solution exists, None if no solution exists
    """
    # Validate board first
    if not is_valid_board(board):
        return None
    
    # Create a copy of the board
    board = [row[:] for row in board]
    
    # Find all empty positions
    empty_pos = [(i, j) for i in range(9) for j in range(9) if board[i][j] == 0]
    
    if solve_helper(board, empty_pos, 0):
        return board
    return None

def solve_helper(board, empty_pos, pos_idx):
    """Optimized helper function for recursive solving"""
    if pos_idx >= len(empty_pos):
        return True
        
    row, col = empty_pos[pos_idx]
    
    # Pre-calculate valid numbers for this position
    for num in range(1, 10):
        if is_safe(board, row, col, num):
            board[row][col] = num
            if solve_helper(board, empty_pos, pos_idx + 1):
                return True
            board[row][col] = 0
            
    return False

def is_safe(board, row, col, num):
    """Optimized safety check"""
    # Check row
    if num in board[row]:
        return False
    
    # Check column
    if num in (board[i][col] for i in range(9)):
        return False
    
    # Check 3x3 box
    box_row, box_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(box_row, box_row + 3):
        for j in range(box_col, box_col + 3):
            if board[i][j] == num:
                return False
    
    return True

def is_valid_board(board):
    """Validate initial board state"""
    if len(board) != 9 or any(len(row) != 9 for row in board):
        return False
    
    # Check for invalid numbers and duplicates in rows
    for row in board:
        nums = [n for n in row if n != 0]
        if any(n < 0 or n > 9 for n in row) or len(nums) != len(set(nums)):
            return False
    
    # Check for duplicates in columns
    for col in range(9):
        nums = [board[row][col] for row in range(9) if board[row][col] != 0]
        if len(nums) != len(set(nums)):
            return False
    
    # Check for duplicates in 3x3 boxes
    for box_row in range(0, 9, 3):
        for box_col in range(0, 9, 3):
            nums = []
            for i in range(box_row, box_row + 3):
                for j in range(box_col, box_col + 3):
                    if board[i][j] != 0:
                        nums.append(board[i][j])
            if len(nums) != len(set(nums)):
                return False
    
    return True