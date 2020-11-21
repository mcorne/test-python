# https://leetcode.com/problems/decode-ways/
class Solution:
    def numDecodings(self, s: str) -> int:
        n = 1 # Combinations ending with a digit, eg 1, 9
        p = 0 # Combinations ending with a pair, eg 10, 26
        prev = None # previous digit if 1 or 2
        for c in s:
            if c == "0":
                if prev is None:
                    # Co previous digit to pair with 0, not a valid message
                    return 0
                # Co more combinations ending with a digit: n -> 0
                # 0 paired with previous digit: p -> n
                n, p = 0, n
            if prev == "1" or prev == "2" and c <= "6":
                # Digit added to both combinations ending with or without a pair: n -> n+p
                # Digit paired with previous digit: p -> n
                n, p = n+p, n
            else:
                # Digit added to both combinations ending with or without a pair: n -> n+p
                # No more combinations ending with a pair: p -> 0
                n, p = n+p, 0
            if c == "1" or c == "2":
                prev = c
            else:
                prev = None
        return n + p

    # Recursive solution that scans all combinations but exeeds the computation time limit for large messages
    def numDecodingsRecursive(self, s: str, index: int = 0) -> int:
        if index == 0:
            self.num = 0
            self.len = len(s)
        if self.len == index:
            self.num += 1
            return
        if s[index] == "0":
            return 0
        self.numDecodings(s, index+1)
        if self.len-index >= 2 and (s[index] == "1" or s[index] == "2" and s[index+1] <= "6"):
            self.numDecodings(s, index+2)
        return self.num

# Tests
def test(s, expected):
    solution = Solution()
    output = solution.numDecodings(s)
    status = "OK" if output == expected else "ERROR"
    print(status, output)

s = "12"
expected = 2
test(s, expected)

s = "226"
expected = 3
test(s, expected)

s = "0"
expected = 0
test(s, expected)

s = "1"
expected = 1
test(s, expected)

s = "10"
expected = 1
test(s, expected)

s = "100"
expected = 0
test(s, expected)

s = "123456"
expected = 3
test(s, expected)

s = "1212"
expected = 5
test(s, expected)

s = "111111111111111111111111111111111111111111111"
expected = 1836311903
test(s, expected)

s = "1"
expected = 1
test(s, expected)

s = "11"
expected = 2
test(s, expected)

s = "111"
expected = 3
test(s, expected)

s = "1111"
expected = 5
test(s, expected)

s = "11111"
expected = 8
test(s, expected)

s = "111111"
expected = 13
test(s, expected)

s = "1111111"
expected = 21
test(s, expected)

s = "11111111"
expected = 34
test(s, expected)

s = "111111111"
expected = 55
test(s, expected)

s = "1111111111"
expected = 89
test(s, expected)

# LeetCode Submission
# Runtime: 32 ms, faster than 60.18% of Python3 online submissions for Decode Ways.
# Memory Usage: 14.3 MB, less than 13.04% of Python3 online submissions for Decode Ways.
# 268 / 268 test cases passed.

# Note that combinations of messages 1, 11, 111, 1111 etc. follow a Fibonacci sequence
# 1: 1
# 11:2
# 111:3
# 1111:5
# 11111:8
# 111111:13
# 1111111:21
# 11111111:34
# 111111111:55
# 1111111111:89
