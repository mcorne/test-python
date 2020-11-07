import re

class Solution:
    def myAtoi(self, s: str) -> int:
        match = re.match(r"^ *([+-])?(\d+)", s)
        if not match:
            return 0
        sign, x = match.groups()
        x = int(x)
        if sign == '-':
            x = -x
        if x < -(2**31) :
            x = -(2**31)
        elif x > (2**31 - 1):
            x = (2**31 - 1)
        return x

# Tests
solution = Solution()
str = "42"
print(solution.myAtoi(str))
str = "   -42"
print(solution.myAtoi(str))
str = "4193 with words"
print(solution.myAtoi(str))
str = "words and 987"
print(solution.myAtoi(str))
str = "-91283472332"
print(solution.myAtoi(str))
str = "1111111111111111111111"
print(solution.myAtoi(str))

# LeetCode Submission
# Runtime: 28 ms, faster than 92.73% of Python3 online submissions for String to Integer (atoi).
# Memory Usage: 14.2 MB, less than 100.00% of Python3 online submissions for String to Integer (atoi).
# 1084 / 1084 test cases passed.
