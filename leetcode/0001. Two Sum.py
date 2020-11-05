class Solution:
    def twoSum(self, nums, target):
        diffs = {}
        for index, num in enumerate(nums):
            if index and num in diffs:
                return [diffs[num], index]
            diffs[target - num] = index

# Tests
s = Solution()
nums = [2,7,11,15]
target = 9
print(s.twoSum(nums, target))
nums = [3,2,4]
target = 6
print(s.twoSum(nums, target))
nums = [3,3]
target = 6
print(s.twoSum(nums, target))

# LeetCode Submission
# Runtime: 48 ms, faster than 76.47% of Python3 online submissions for Two Sum.
# Memory Usage: 15.3 MB, less than 17.54% of Python3 online submissions for Two Sum.
# 29 / 29 test cases passed.