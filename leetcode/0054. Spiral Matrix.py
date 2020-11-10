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
solution = Solution()
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(solution.spiralOrder(matrix))
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9,10,11,12]
]
print(solution.spiralOrder(matrix))
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12]
]
print(solution.spiralOrder(matrix))
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]
print(solution.spiralOrder(matrix))
matrix = []
print(solution.spiralOrder(matrix))
matrix = [[1]]
print(solution.spiralOrder(matrix))
matrix = [[1, 2, 3]]
print(solution.spiralOrder(matrix))
matrix = [
    [1],
    [2],
    [2]
]
print(solution.spiralOrder(matrix))

# LeetCode Submission
# Runtime: 24 ms, faster than 94.04% of Python3 online submissions for Spiral Matrix.
# Memory Usage: 14.2 MB, less than 100.00% of Python3 online submissions for Spiral Matrix.
# 22 / 22 test cases passed.
