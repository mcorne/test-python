from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        return 0


# Tests
def test(height, expected):
    solution = Solution()
    is_valid = solution.maxArea(height)
    status = "OK" if is_valid == expected else "ERROR"
    print(status, is_valid)


# Tests
s = "()"
expected = True
test(s, expected)

# LeetCode Submission
# ....
