class Solution:
    def canFormArray(self, arr, pieces):
        arr_len = len(arr)
        index = 0
        while True:
            remainder = arr[index:]
            found_piece = False
            for piece in pieces:
                piece_len = len(piece)
                if piece_len <= len(remainder) and remainder[:piece_len] == piece:
                    index += piece_len
                    found_piece = True
                    break
            if not found_piece:
                return False
            if index == arr_len:
                return True

# Tests
s = Solution()
arr = [85]
pieces = [[85]]
print(s.canFormArray(arr, pieces))
arr = [15,88]
pieces = [[88],[15]]
print(s.canFormArray(arr, pieces))
arr = [49,18,16]
pieces = [[16,18,49]]
print(s.canFormArray(arr, pieces))
arr = [91,4,64,78]
pieces = [[78],[4,64],[91]]
print(s.canFormArray(arr, pieces))

# LeetCode Submission
# Runtime: 36 ms, faster than 95.41% of Python3 online submissions for Check Array Formation Through Concatenation.
# Memory Usage: 14.1 MB, less than 100.00% of Python3 online submissions for Check Array Formation Through Concatenation.
# 82 / 82 test cases passed.