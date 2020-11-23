from typing import List

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        last_i = len(board) - 1
        last_j = len(board[0]) - 1
        # Zero cells from left to right
        prev = None
        for i in range(0, last_i+1):
            for j in range(0, last_j+1):
                if board[i][j] == "O" and (prev == "Z" or i == 0 or i == last_i or j == 0 or j == last_j):
                    prev, board[i][j] = board[i][j], "Z"
        # Zero cells from right to left
        prev = None
        for i in range(0, last_i+1):
            for j in range(last_j, -1, -1):
                if board[i][j] == "O" and (prev == "Z" or i == 0 or i == last_i or j == 0 or j == last_j):
                    prev, board[i][j] = board[i][j], "Z"
        # Zero cells from top to bottom
        prev = None
        for j in range(0, last_j+1):
            for i in range(0, last_i+1):
                if board[i][j] == "O" and (prev == "Z" or i == 0 or i == last_i or j == 0 or j == last_j):
                    prev, board[i][j] = board[i][j], "Z"
        # Zero cells from bottom to top
        for j in range(0, last_j+1):
            for i in range(last_i, -1, -1):
                if board[i][j] == "O" and (prev == "Z" or i == 0 or i == last_i or j == 0 or j == last_j):
                    prev, board[i][j] = board[i][j], "Z"
        # Changes non zeroed cells ("O") to surrounded ("X") and zeroed cells ("Z") to not surrounded ("O")
        for i in range(0, last_i+1):
            for j in range(0, last_j+1):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "Z":
                    board[i][j] = "O"


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
X X X X X O O X X X X X X O X X
X O O X X O O X X O O X X O O X
X O O X X O O X X O O X X O O X
X O O X X O O X X O O X X O O X
X O O X X O O X X O O X X O O X
X O O X X O O X X O O X X O O X
X O O X X O O X X O O X X O O X
X O O X X O O X X O O X X O O X
X O O X X O O X X O O X X O O X
X O O X X O O X X O O X X O O X
X O O X X O O X X O O X X O O X
"""
expected = """
X X X X
X X X X
X X X X
X O X X
"""
test(board, expected)

# LeetCode Submission
