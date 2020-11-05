class Solution:
    def isPalindrome(self, x):
        if x < 0:
            return False
        x = str(x)
        half_length = len(x) >> 1
        left = x[0:half_length]
        reversed_right = x[::-1][0:half_length]
        return left == reversed_right

# Tests
s = Solution()
x = 121
print(s.isPalindrome(x))
x = -121
print(s.isPalindrome(x))
x = 10
print(s.isPalindrome(x))
x = -101
print(s.isPalindrome(x))
x = 100
print(s.isPalindrome(x))
x = 1221
print(s.isPalindrome(x))

# LeetCode Submission
# Runtime: 64 ms, faster than 54.65% of Python3 online submissions for Palindrome Number.
# Memory Usage: 14.1 MB, less than 100.00% of Python3 online submissions for Palindrome Number.
# 11510 / 11510 test cases passed.
