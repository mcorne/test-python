# https://leetcode.com/problems/decode-ways/
class Solution:
    def numDecodings(self, s: str, index: int = 0) -> int:
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

# s = "12"
# expected = 2
# test(s, expected)

# s = "226"
# expected = 3
# test(s, expected)

# s = "0"
# expected = 0
# test(s, expected)

# s = "1"
# expected = 1
# test(s, expected)

# s = "100"
# expected = 0
# test(s, expected)

# s = "123456"
# expected = 3
# test(s, expected)

# s = "1212"
# expected = 5
# test(s, expected)

# s = "111111111111111111111111111111111111111111111"
# expected = 5
# test(s, expected)

s = "111111111111111111111111111111"
expected = 8
test(s, expected)

# LeetCode Submission
# Error: Time Limit Exceeded
# Last executed input: "111111111111111111111111111111111111111111111"
