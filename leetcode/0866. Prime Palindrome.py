from math import sqrt
class Solution:
    def primePalindrome(self, N: int) -> int:
        if N == 1 or N == 2:
            return 2
        if N == 3:
            return 3
        if N % 2 == 0:
            N += 1
        while True:
            s = str(N)
            if s == s[::-1]:
                i = 3
                is_prime = True
                # see https://en.wikipedia.org/wiki/Trial_division
                sqrt_N = sqrt(N)
                while i <= sqrt_N:
                    if N % i == 0:
                        is_prime = False
                        break
                    i += 2
                if is_prime:
                    return N
            N += 2

# Tests
solution = Solution()
N = 6
print(solution.primePalindrome(N))
N = 8
print(solution.primePalindrome(N))
N = 13
print(solution.primePalindrome(N))
N = 1
print(solution.primePalindrome(N))
N = 2
print(solution.primePalindrome(N))
N = 1000000
print(solution.primePalindrome(N))
N = 9989900
print(solution.primePalindrome(N))

# LeetCode Submission
# Error: Time Limit Exceeded.
# 51 / 60 test cases passed.
# Last executed input: 9989900

# https://primes.utm.edu/howmany.html
# 5,761,455 prime numbers <= 10^8
# https://oeis.org/A002113/b002113.txt
# 19,999 palindromes <= 10^8
# https://oeis.org/A002385/b002385.txt
# 100030001 next prime palindrome after 10^8 (782th)
