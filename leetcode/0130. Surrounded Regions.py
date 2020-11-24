from typing import List

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if board == []:
            return board
        self.board = board
        self.height = len(board)
        self.width = len(board[0])
        # Zero "O" connected cells starting from horizontal edges
        for i in range(0, self.height):
            if self.board[i][0] == "O":
                self.zero_O_cell(i, 0)
            if self.board[i][self.width-1] == "O":
                self.zero_O_cell(i, self.width-1)
        # Zero "O" connected cells starting from vertical edges
        for j in range(1, self.width-1):
            if self.board[0][j] == "O":
                self.zero_O_cell(0, j)
            if self.board[self.height-1][j] == "O":
                self.zero_O_cell(self.height-1, j)
        # Changes non zeroed cells ("O") to surrounded ("X") and zeroed cells ("Z") to not surrounded ("O")
        for i in range(0, self.height):
            for j in range(0, self.width):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "Z":
                    board[i][j] = "O"

    def zero_O_cell(self, i: int, j: int):
        self.board[i][j] = "Z"
        above = i - 1
        if above >= 0 and self.board[above][j] == "O":
            self.zero_O_cell(above, j)
        below = i + 1
        if below < self.height and self.board[below][j] == "O":
            self.zero_O_cell(below, j)
        left = j - 1
        if left >= 0 and self.board[i][left] == "O":
            self.zero_O_cell(i, left)
        right = j + 1
        if right < self.width and self.board[i][right] == "O":
            self.zero_O_cell(i, right)

    def list2string(self, lst: List[List[str]]) -> str:
        return "\n".join([" ".join(row) for row in lst])

    def string2list(self, str: str) -> List[List[str]]:
        return [list(s.replace(" ", "")) for s in str.strip().splitlines()]

# Tests
def test(board, expected):
    solution = Solution()
    board = solution.string2list(board)
    expected = solution.string2list(expected)
    solution.solve(board)
    status = "OK" if board == expected else "ERROR"
    print(status, solution.list2string(board), sep="\n")

board = """
X X X X
X O O X
X X O X
X O X X
"""
expected = """
X X X X
X X X X
X X X X
X O X X
"""
test(board, expected)

board = """
X O X X X X X X
X O O X X O O X
X X X X X X X X
X X X X X O O X
X X X X X X X X
X O O O X X O O
O O X O X X X X
X X X X X O O X
X X X O X O O O
X X X O X X X X
"""
expected = """
X O X X X X X X
X O O X X X X X
X X X X X X X X
X X X X X X X X
X X X X X X X X
X O O O X X O O
O O X O X X X X
X X X X X O O X
X X X O X O O O
X X X O X X X X
"""
test(board, expected)

board = """
X
"""
expected = """
X
"""
test(board, expected)

board = """
O
"""
expected = """
O
"""
test(board, expected)

board = """
O X
"""
expected = """
O X
"""
test(board, expected)

board = """
O
X
"""
expected = """
O
X
"""
test(board, expected)

board = """
X O X X X
X O O O X
X O X O X
X O O O X
X O X X X
"""
expected = """
X O X X X
X O O O X
X O X O X
X O O O X
X O X X X
"""
test(board, expected)

board = """
O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O
O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O
O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O
O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O
O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O
O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O
O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O
O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O
O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O
O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O
O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O
O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O
O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O
O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O
O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O
O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O
O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O
O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O
O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O
O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O
O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O
O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O
O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O
O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O
O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O
O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O
O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O
O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O
O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O
"""
expected = """
O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O
O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O
O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O
O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O
O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O
O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O
O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O
O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O
O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O
O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O
O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O
O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O
O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O
O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O
O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O
O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O
O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O
O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O
O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O
O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O
O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O
O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O
O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O
O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O
O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O
O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O
O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O
O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O
O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O
"""
test(board, expected)

# LeetCode Submission
# Runtime: 136 ms, faster than 63.46% of Python3 online submissions for Surrounded Regions.
# Memory Usage: 16.1 MB, less than 26.01% of Python3 online submissions for Surrounded Regions.
# 59 / 59 test cases passed.
