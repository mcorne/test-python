# https://leetcode.com/problems/sudoku-solver/
from typing import List

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        self.board = board
        self.fix_dots()
        self.backup = False
        self.fix_board()
        self.backup = []
        self.solve_board()

    def fix_board(self):
        for i in range(9):
            for j in range(9):
                if type(self.board[i][j]) == str:
                    self.fix_row_col_block(i, j)

    def fix_cells(self, x, y, start_i, stop_i, start_j, stop_j):
        for i in range(start_i, stop_i):
            for j in range(start_j, stop_j):
                if i != x or j != y:
                    if type(self.board[i][j]) == str:
                        if self.board[i][j] == self.board[x][y]:
                            return False
                    else:
                        try:
                            self.board[i][j].remove(self.board[x][y])
                        except ValueError:
                            continue
                        if self.backup != False:
                            if self.backup:
                                self.backup[-1].append([i, j, self.board[x][y]])
                            else:
                                self.backup.append([[i, j, self.board[x][y]]])
                        if not self.board[i][j]:
                            return False
        return True

    def fix_dots(self):
        for i in range(9):
            for j in range(9):
                if self.board[i][j] == ".":
                    self.board[i][j] = [str(i) for i in range(1, 10)]

    def fix_row_col_block(self, i, j):
        if not self.fix_cells(i, j, i, i+1, 0, 9): # fix row
            return False
        if not self.fix_cells(i, j, 0, 9, j, j+1): # fix column
            return False
        start_i, start_j = i//3*3, j//3*3
        if not self.fix_cells(i, j, start_i, start_i+3, start_j, start_j+3): # fix block
            return False
        return True

    def restore_board(self):
        for i, j, value in self.backup.pop():
            if type(value) == list:
                self.board[i][j] = value
            else:
                if type(self.board[i][j]) == str:
                    self.board[i][j] = [self.board[i][j]]
                self.board[i][j].append(value)

    def solve_board(self, start_i=0, start_j=0):
        for i in range(start_i, 9):
            for j in range(start_j, 9):
                if type(self.board[i][j]) == list:
                    values = self.board[i][j]
                    for value in values:
                        self.backup.append([[i, j, values]])
                        self.board[i][j] = value
                        if self.fix_row_col_block(i, j):
                            if j < 8:
                                next_i, next_j = i, j+1
                            else:
                                next_i, next_j = i+1, 0
                            if self.solve_board(next_i, next_j):
                                return True
                        if self.backup:
                            self.restore_board()
                    return False
            start_j = 0
        return True

# Tests
def test(board, expected):
    solution = Solution()
    solution.solveSudoku(board)
    status = "OK" if board == expected else "ERROR"
    print(status, board)

board = [
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]
expected = [
    ["5","3","4","6","7","8","9","1","2"],
    ["6","7","2","1","9","5","3","4","8"],
    ["1","9","8","3","4","2","5","6","7"],
    ["8","5","9","7","6","1","4","2","3"],
    ["4","2","6","8","5","3","7","9","1"],
    ["7","1","3","9","2","4","8","5","6"],
    ["9","6","1","5","3","7","2","8","4"],
    ["2","8","7","4","1","9","6","3","5"],
    ["3","4","5","2","8","6","1","7","9"]
]
test(board, expected)

# LeetCode Submission
# Runtime: 188 ms, faster than 71.17% of Python3 online submissions for Sudoku Solver.
# Memory Usage: 14.5 MB, less than 13.48% of Python3 online submissions for Sudoku Solver.
# 6 / 6 test cases passed.
