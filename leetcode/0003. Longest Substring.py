class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        while s:
            length = 0
            substring = {}
            for c in s:
                if c in substring:
                    break
                length += 1
                substring[c] = True
            if length > max_length:
                max_length = length
            s = s[1:]
        return max_length


# Tests
solution = Solution()
s = "abcabcbb"
print(solution.lengthOfLongestSubstring(s))
s = "bbbbb"
print(solution.lengthOfLongestSubstring(s))
s = "pwwkew"
print(solution.lengthOfLongestSubstring(s))
s = ""
print(solution.lengthOfLongestSubstring(s))
s = " "
print(solution.lengthOfLongestSubstring(s))
s = "dvdf"
print(solution.lengthOfLongestSubstring(s))

# LeetCode Submission
# Runtime: 412 ms, faster than 16.29% of Python3 online submissions for Longest Substring Without Repeating Characters.
# Memory Usage: 14.3 MB, less than 100.00% of Python3 online submissions for Longest Substring Without Repeating Characters.
# 987 / 987 test cases passed.