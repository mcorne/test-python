from bisect import bisect_left
from math import sqrt

class Solution:
    palindromes = None

    def __init__(self) -> None:
        if not Solution.palindromes:
            Solution.palindromes = self.generatePalindromes()

    # https://leetcode.com/problems/prime-palindrome/discuss/868157/Python-creating-palindrome-list
    def generatePalindromes(self) -> list:
        pals = [[] for i in range(9)]
        pals[0] = ['0','1','2','3','4','5','6','7','8','9']
        pals[1] =['00','11','22','33','44','55','66','77','88','99']
        for i in range(2,8):
            pals[i] = [x[0]+y+x[1] for y in pals[i-2] for x in pals[1]]
        pals[8] = ['1'+y+'1' for y in pals[6]] # need only 10^8 range
        palindromes = sorted(int(x) for y in pals for x in y)
        return palindromes

    # see https://en.wikipedia.org/wiki/Trial_division
    def isPrime(self, N: int) -> bool:
        if N % 2 == 0:
            return False
        i = 3
        sqrt_N = sqrt(N)
        while i <= sqrt_N:
            if N % i == 0:
                return False
            i += 2
        return True

    def primePalindrome(self, N: int) -> int:
        if N == 1 or N == 2:
            return 2
        for N in Solution.palindromes[bisect_left(Solution.palindromes,N):]:
            if self.isPrime(N):
                return(N)

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
N = 3
print(solution.primePalindrome(N))
N = 1000000
print(solution.primePalindrome(N))
N = 9989900
print(solution.primePalindrome(N))

# LeetCode Submission
# Runtime: 56 ms, faster than 87.95% of Python3 online submissions for Prime Palindrome.
# Memory Usage: 17 MB, less than 9.64% of Python3 online submissions for Prime Palindrome.
# 60 / 60 test cases passed.

# https://primes.utm.edu/howmany.html
# 5,761,455 prime numbers <= 10^8
# https://oeis.org/A002113/b002113.txt
# 19,999 palindromes <= 10^8
# https://oeis.org/A002385/b002385.txt
# 100030001 next prime palindrome after 10^8 (782th)
