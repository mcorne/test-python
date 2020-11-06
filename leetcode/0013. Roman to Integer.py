import re

class Solution:
    symbols = {
        # two letter symbols on top
        "CD": 400,
        "CM": 900,
        "IV": 4,
        "IX": 9,
        "XC": 90,
        "XL": 40,
        # one letter symbols after
        "C": 100,
        "D": 500,
        "I": 1,
        "L": 50,
        "M": 1000,
        "V": 5,
        "X": 10,
    }

    def __init__(self):
        self.pattern = "(" + "|".join(Solution.symbols.keys()) + ")"

    def romanToInt(self, s: str) -> int:
        value = 0
        for match in re.finditer(self.pattern, s, re.I):
            symbol = match.group()
            value += Solution.symbols[symbol]
        return value

# Tests
s = Solution()
r = "III"
print(s.romanToInt(r))
r = "IV"
print(s.romanToInt(r))
r = "IX"
print(s.romanToInt(r))
r = "LVIII"
print(s.romanToInt(r))
r = "MCMXCIV"
print(s.romanToInt(r))

# LeetCode Submission
# Runtime: 60 ms, faster than 13.93% of Python3 online submissions for Roman to Integer.
# Memory Usage: 14.1 MB, less than 100.00% of Python3 online submissions for Roman to Integer.
# 3999 / 3999 test cases passed.