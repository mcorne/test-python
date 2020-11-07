class Solution:
    def convert(self, s: str, numRows: int) -> str:
        lines = ["" for i in range(numRows)]
        down = True
        i = 0       
        numRows -= 1         
        for c in s:
            lines[i] += c
            if down:
                if i < numRows:
                    i += 1
                else:
                    i -= 1
                    down = False
            else:
                if i > 0:
                    i -= 1
                else:
                    i += 1
                    down = True
        return "".join(lines)

# Tests
solution = Solution()
s = "PAYPALISHIRING"
numRows = 3
print(solution.convert(s, numRows))
s = "PAYPALISHIRING"
numRows = 4
print(solution.convert(s, numRows))
s = "A"
numRows = 1
print(solution.convert(s, numRows))

# LeetCode Submission
# Runtime: 44 ms, faster than 98.06% of Python3 online submissions for ZigZag Conversion.
# Memory Usage: 14.2 MB, less than 6.93% of Python3 online submissions for ZigZag Conversion.
# 1157 / 1157 test cases passed.