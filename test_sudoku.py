import unittest
from sudoku import solve_sudoku

class TestSudokuSolver(unittest.TestCase):
    def verify_solution(self, solution):
        """Helper method to verify if a solution is valid"""
        if solution is None:
            return False
            
        # Check rows
        for row in solution:
            if sorted(row) != list(range(1, 10)):
                return False
                
        # Check columns
        for col in range(9):
            column = [solution[row][col] for row in range(9)]
            if sorted(column) != list(range(1, 10)):
                return False
                
        # Check 3x3 boxes
        for box_row in range(0, 9, 3):
            for box_col in range(0, 9, 3):
                box = []
                for i in range(3):
                    for j in range(3):
                        box.append(solution[box_row + i][box_col + j])
                if sorted(box) != list(range(1, 10)):
                    return False
                    
        return True

    def test_puzzle1(self):
        """Test a simple puzzle"""
        board = [
            [5,3,0,0,7,0,0,0,0],
            [6,0,0,1,9,5,0,0,0],
            [0,9,8,0,0,0,0,6,0],
            [8,0,0,0,6,0,0,0,3],
            [4,0,0,8,0,3,0,0,1],
            [7,0,0,0,2,0,0,0,6],
            [0,6,0,0,0,0,2,8,0],
            [0,0,0,4,1,9,0,0,5],
            [0,0,0,0,8,0,0,7,9]
        ]
        result = solve_sudoku(board)
        self.assertTrue(self.verify_solution(result))

    def test_puzzle2(self):
        """Test a medium puzzle"""
        board = [
            [0,0,0,2,6,0,7,0,1],
            [6,8,0,0,7,0,0,9,0],
            [1,9,0,0,0,4,5,0,0],
            [8,2,0,1,0,0,0,4,0],
            [0,0,4,6,0,2,9,0,0],
            [0,5,0,0,0,3,0,2,8],
            [0,0,9,3,0,0,0,7,4],
            [0,4,0,0,5,0,0,3,6],
            [7,0,3,0,1,8,0,0,0]
        ]
        result = solve_sudoku(board)
        self.assertTrue(self.verify_solution(result))

    def test_puzzle3(self):
        """Test another medium puzzle"""
        board = [
            [0,0,0,6,0,0,4,0,0],
            [7,0,0,0,0,3,6,0,0],
            [0,0,0,0,9,1,0,8,0],
            [0,0,0,0,0,0,0,0,0],
            [0,5,0,1,8,0,0,0,3],
            [0,0,0,3,0,6,0,4,5],
            [0,4,0,2,0,0,0,6,0],
            [9,0,3,0,0,0,0,0,0],
            [0,2,0,0,0,0,1,0,0]
        ]
        result = solve_sudoku(board)
        self.assertTrue(self.verify_solution(result))

    def test_puzzle4(self):
        """Test a harder puzzle"""
        board = [
            [1,0,0,0,0,7,0,9,0],
            [0,3,0,0,2,0,0,0,8],
            [0,0,9,6,0,0,5,0,0],
            [0,0,5,3,0,0,9,0,0],
            [0,1,0,0,8,0,0,0,2],
            [6,0,0,0,0,4,0,0,0],
            [3,0,0,0,0,0,0,1,0],
            [0,4,0,0,0,0,0,0,7],
            [0,0,7,0,0,0,3,0,0]
        ]
        result = solve_sudoku(board)
        self.assertTrue(self.verify_solution(result))

    def test_puzzle5(self):
        """Test another hard puzzle"""
        board = [
            [8,0,0,0,0,0,0,0,0],
            [0,0,3,6,0,0,0,0,0],
            [0,7,0,0,9,0,2,0,0],
            [0,5,0,0,0,7,0,0,0],
            [0,0,0,0,4,5,7,0,0],
            [0,0,0,1,0,0,0,3,0],
            [0,0,1,0,0,0,0,6,8],
            [0,0,8,5,0,0,0,1,0],
            [0,9,0,0,0,0,4,0,0]
        ]
        result = solve_sudoku(board)
        self.assertTrue(self.verify_solution(result))

    def test_puzzle6(self):
        """Test an invalid board"""
        board = [
            [5,5,0,0,7,0,0,0,0],  # Note the duplicate 5 in first row
            [6,0,0,1,9,5,0,0,0],
            [0,9,8,0,0,0,0,6,0],
            [8,0,0,0,6,0,0,0,3],
            [4,0,0,8,0,3,0,0,1],
            [7,0,0,0,2,0,0,0,6],
            [0,6,0,0,0,0,2,8,0],
            [0,0,0,4,1,9,0,0,5],
            [0,0,0,0,8,0,0,7,9]
        ]
        result = solve_sudoku(board)
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()