class Solution:
    def largestTimeFromDigits(self, arr: list) -> str:
        arr.sort(reverse=True)
        h1_list, h2_h1is2_list, h2_h1not2_list, m1_list, m2_list = [], [], [], [], []
        counts = {}
        for digit in arr:
            if digit in counts:
                counts[digit] += 1
            else:
                counts[digit] = 1

            if digit <= 2:
                h1_list.append(digit)
            if digit <= 3:
                h2_h1is2_list.append(digit)
            if digit <= 5:
                m1_list.append(digit)
            h2_h1not2_list.append(digit)
            m2_list.append(digit)

        for h1 in h1_list:
            counts[h1] -= 1
            h2_list = h2_h1is2_list if h1 == 2 else h2_h1not2_list
            for h2 in h2_list:
                if counts[h2]:
                    counts[h2] -= 1
                    for m1 in m1_list:
                        if counts[m1]:
                            counts[m1] -= 1
                            for m2 in m2_list:
                                if counts[m2]:
                                    return str(h1) + str(h2) + ":" + str(m1) + str(m2)
                            counts[m1] += 1
                    counts[h2] += 1
            counts[h1] += 1
        return ""

# Tests
solution = Solution()
A = [1,2,3,4]
print(solution.largestTimeFromDigits(A))
A = [5,5,5,5]
print(solution.largestTimeFromDigits(A))
A = [0,0,0,0]
print(solution.largestTimeFromDigits(A))
A = [0,0,1,0]
print(solution.largestTimeFromDigits(A))
A = [1,1,3,4]
print(solution.largestTimeFromDigits(A))
A = [1,9,9,8]
print(solution.largestTimeFromDigits(A))
A = [1,9,9,1]
print(solution.largestTimeFromDigits(A))
A = [1,5,5,1]
print(solution.largestTimeFromDigits(A))

# LeetCode Submission
# Runtime: 28 ms, faster than 89.74% of Python3 online submissions for Largest Time for Given Digits.
# Memory Usage: 14.3 MB, less than 100.00% of Python3 online submissions for Largest Time for Given Digits.
# 172 / 172 test cases passed.
