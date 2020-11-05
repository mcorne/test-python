class Solution:
    def reverse(self, x):
        if x >= 0:
            negative = False
        else:
            negative = True
            x = -x
        x = str(x)
        x = int(x[::-1])
        if negative:
            x = -x
        if x < -(2**31) or x > (2**31 - 1):
            return 0
        return x
        

# Tests
s = Solution()
x = 123
print(s.reverse(x))
x = -123
print(s.reverse(x))
x = 120
print(s.reverse(x))
x = 0
print(s.reverse(x))
x = 1534236469
print(s.reverse(x))

# LeetCode Submission
# Runtime: 28 ms, faster than 85.13% of Python3 online submissions for Reverse Integer.
# Memory Usage: 14.1 MB, less than 99.99% of Python3 online submissions for Reverse Integer.
# 1032 / 1032 test cases passed.