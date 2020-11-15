from enum import Enum
from typing import List

class Direction(Enum):
     DOWN = 0
     LEFT = 1
     RIGHT = 2
     TOP = 3

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        width = len(matrix[0])
        height = len(matrix)
        todo = [[True for j in range(width)] for i in range(height)]
        todo_count = width * height
        spiral = []
        i, j = 0, -1
        last_i, last_j = height-1, width-1
        direction = Direction.RIGHT
        while todo_count:
            while True:
                if direction == Direction.RIGHT:
                    if j != last_j and todo[i][j+1]:
                        j += 1
                        break
                    direction = Direction.DOWN
                if direction == Direction.DOWN:
                    if i != last_i and todo[i+1][j]:
                        i += 1
                        break
                    direction = Direction.LEFT
                if direction == Direction.LEFT:
                    if j != 0 and todo[i][j-1]:
                        j -= 1
                        break
                    direction = Direction.TOP
                if direction == Direction.TOP:
                    if i != 0 and todo[i-1][j]:
                        i -= 1
                        break
                    direction = Direction.RIGHT
            todo[i][j] = False
            spiral.append(matrix[i][j])
            todo_count -= 1
        return spiral

# Tests
def test(matrix, expected):
    solution = Solution()
    output = solution.spiralOrder(matrix)
    status = "OK" if output == expected else "ERROR"
    print(status, output)

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
expected = [1, 2, 3, 6, 9, 8, 7, 4, 5]
test(matrix, expected)

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9,10,11,12]
]
expected = [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
test(matrix, expected)

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12]
]
expected = [1, 2, 3, 6, 9, 12, 11, 10, 7, 4, 5, 8]
test(matrix, expected)

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]
expected = [1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10]
test(matrix, expected)

matrix = []
expected = []
test(matrix, expected)

matrix = [[1]]
expected = [1]
test(matrix, expected)

matrix = [[1, 2, 3]]
expected = [1, 2, 3]
test(matrix, expected)

matrix = [
    [1],
    [2],
    [3]
]
expected = [1, 2, 3]
test(matrix, expected)

# LeetCode Submission
# Runtime: 24 ms, faster than 94.04% of Python3 online submissions for Spiral Matrix.
# Memory Usage: 14.2 MB, less than 100.00% of Python3 online submissions for Spiral Matrix.
# 22 / 22 test cases passed.
