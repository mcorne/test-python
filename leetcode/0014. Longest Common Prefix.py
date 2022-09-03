# https://leetcode.com/problems/longest-common-prefix/
from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs.pop(0)
        for string in strs:
            chars = ""
            for i in range(min(len(prefix), len(string))):
                if string[i] != prefix[i]:
                    break
                chars += string[i]
            prefix = chars
            if len(prefix) == 0:
                break
        return prefix

# Tests
def test(strs, expected):
    solution = Solution()
    prefix = solution.longestCommonPrefix(strs)
    status = "OK" if prefix == expected else "ERROR"
    print(status, prefix)

# Tests
strs = ["flower","flow","flight"]
expected = "fl"
test(strs, expected)

strs = ["dog","racecar","car"]
expected = ""
test(strs, expected)

strs = ["dog"]
expected = "dog"
test(strs, expected)

strs = [""]
expected = ""
test(strs, expected)

expected = "".join(["a" for i in range(200)])
strs = [expected for i in range(200)]
test(strs, expected)

# LeetCode Submission
# Runtime: 76 ms, faster than 10.15% of Python3 online submissions for Longest Common Prefix.
# Memory Usage: 13.9 MB, less than 88.34% of Python3 online submissions for Longest Common Prefix.
