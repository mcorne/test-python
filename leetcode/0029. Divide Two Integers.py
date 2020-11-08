class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        negative = False
        if dividend < 0:
            negative = True
            dividend = -dividend
        if divisor < 0:
            divisor = -divisor
            negative = not negative

        length = len(str(divisor)) - 1
        dividend = str(dividend)
        digits = dividend[length:]
        dividend = dividend[0:length]
        quotient_str = "0"
        for digit in digits:
            dividend += digit
            sub_quotient, dividend = self.sub_divide(int(dividend), divisor)
            quotient_str += sub_quotient
        quotient = int(quotient_str)

        if negative:
            quotient = -quotient
        if quotient < -(2**31) :
            quotient = -(2**31)
        elif quotient > (2**31 - 1):
            quotient = (2**31 - 1)
        return quotient


    def sub_divide(self, remainder: int, divisor: int) -> list:
        quotient = 0
        while remainder >= divisor:
            remainder -= divisor
            quotient += 1
        return [str(quotient), str(remainder)]

# Tests
solution = Solution()
dividend = 10
divisor = 3
print(solution.divide(dividend, divisor))
dividend = 7
divisor = -3
print(solution.divide(dividend, divisor))
dividend = 0
divisor = 1
print(solution.divide(dividend, divisor))
dividend = 1
divisor = 1
print(solution.divide(dividend, divisor))
dividend = 21
divisor = 2
print(solution.divide(dividend, divisor))
dividend = 11111111
divisor = 1
print(solution.divide(dividend, divisor))
dividend = 4560
divisor = 56
print(solution.divide(dividend, divisor))
dividend = 20370
divisor = 16
print(solution.divide(dividend, divisor))
dividend = 2147483647
divisor = 2
print(solution.divide(dividend, divisor))
dividend = 102137742
divisor = 1817624734
print(solution.divide(dividend, divisor))

# LeetCode Submission
# Runtime: 36 ms, faster than 37.09% of Python3 online submissions for Divide Two Integers.
# Memory Usage: 14.2 MB, less than 100.00% of Python3 online submissions for Divide Two Integers.
# 989 / 989 test cases passed.
