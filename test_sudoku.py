import unittest
from sudoku import solve_sudoku

class TestSudokuSolver(unittest.TestCase):
    def test_wikipedia_puzzle(self):
        # Test case from Wikipedia
        initial_board = [
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
        
        expected_solution = [
            [5,3,4,6,7,8,9,1,2],
            [6,7,2,1,9,5,3,4,8],
            [1,9,8,3,4,2,5,6,7],
            [8,5,9,7,6,1,4,2,3],
            [4,2,6,8,5,3,7,9,1],
            [7,1,3,9,2,4,8,5,6],
            [9,6,1,5,3,7,2,8,4],
            [2,8,7,4,1,9,6,3,5],
            [3,4,5,2,8,6,1,7,9]
        ]
        
        solution = solve_sudoku(initial_board)
        self.assertEqual(solution, expected_solution)
    
    def test_empty_puzzle(self):
        # Test completely empty puzzle
        initial_board = [[0]*9 for _ in range(9)]
        solution = solve_sudoku(initial_board)
        self.assertIsNotNone(solution)
        # Verify solution is valid
        for i in range(9):
            self.assertEqual(set(solution[i]), set(range(1, 10)))
    
    def test_invalid_board_size(self):
        # Test invalid board size
        invalid_board = [[0]*8 for _ in range(8)]  # 8x8 instead of 9x9
        solution = solve_sudoku(invalid_board)
        self.assertIsNone(solution)
    
    def test_invalid_numbers(self):
        # Test board with invalid numbers
        invalid_board = [
            [5,3,0,0,7,0,0,0,0],
            [6,0,0,1,9,5,0,0,0],
            [0,9,8,0,0,0,0,6,0],
            [8,0,0,0,6,0,0,0,3],
            [4,0,0,8,0,3,0,0,1],
            [7,0,0,0,2,0,0,0,6],
            [0,6,0,0,0,0,2,8,0],
            [0,0,0,4,1,9,0,0,10],  # 10 is invalid
            [0,0,0,0,8,0,0,7,9]
        ]
        solution = solve_sudoku(invalid_board)
        self.assertIsNone(solution)
    
    def test_unsolvable_puzzle(self):
        # Test unsolvable puzzle
        unsolvable_board = [
            [5,3,0,0,7,0,0,0,0],
            [5,0,0,1,9,5,0,0,0],  # Note the duplicate 5 in column 1
            [0,9,8,0,0,0,0,6,0],
            [8,0,0,0,6,0,0,0,3],
            [4,0,0,8,0,3,0,0,1],
            [7,0,0,0,2,0,0,0,6],
            [0,6,0,0,0,0,2,8,0],
            [0,0,0,4,1,9,0,0,5],
            [0,0,0,0,8,0,0,7,9]
        ]
        solution = solve_sudoku(unsolvable_board)
        self.assertIsNone(solution)
    
    def test_already_solved_puzzle(self):
        # Test already solved puzzle
        solved_board = [
            [5,3,4,6,7,8,9,1,2],
            [6,7,2,1,9,5,3,4,8],
            [1,9,8,3,4,2,5,6,7],
            [8,5,9,7,6,1,4,2,3],
            [4,2,6,8,5,3,7,9,1],
            [7,1,3,9,2,4,8,5,6],
            [9,6,1,5,3,7,2,8,4],
            [2,8,7,4,1,9,6,3,5],
            [3,4,5,2,8,6,1,7,9]
        ]
        solution = solve_sudoku(solved_board)
        self.assertEqual(solution, solved_board)

if __name__ == '__main__':
    unittest.main()