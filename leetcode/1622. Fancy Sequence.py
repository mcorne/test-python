# https://leetcode.com/problems/fancy-sequence/
class Fancy:
    def __init__(self):
        self.inc = 0
        self.m = 1
        self.modulus = 10**9 + 7
        self.values = []

    def append(self, value: int) -> None:
        self.values.append([value, self.m, self.inc])

    def addAll(self, inc: int) -> None:
        self.inc += inc
        self.inc %= self.modulus

    def multAll(self, m: int) -> None:
        self.m *= m
        self.m %= self.modulus
        self.inc *= m
        self.inc %= self.modulus

    def getIndex(self, idx: int) -> int:
        if idx >= len(self.values):
            return -1
        value, m, inc = self.values[idx]
        # Modular inverse where the modulus is a prime: a**(-1) ≡ a**(m-2) (mod m)
        # https://en.wikipedia.org/wiki/Modular_multiplicative_inverse#Using_Euler's_theorem
        # m = self.m / m = self.m * m**(-1)
        m = self.m * pow(m, self.modulus-2, self.modulus)
        inc = self.inc - inc * m
        value = value * m + inc
        return int(value % self.modulus)

    @classmethod
    def generateSequence(cls, methods: list, args: list) -> list:
        sequence = []
        for method, arg in zip(methods, args):
            if method == "Fancy":
                fancy = cls()
                sequence.append(None)
            else:
                action = getattr(fancy, method)
                sequence.append(action(arg[0]))
        return sequence

# Tests
def test(methods, args, expected = None):
    sequence = Fancy.generateSequence(methods, args)
    if expected is None:
        status = "NO CHECK - TIME TEST"
        sequence = sequence[:20] + ["..."]
    elif expected == sequence:
        status = "OK"
    else:
        status = "ERROR"
    print(status, sequence)

methods = ["Fancy", "append", "addAll", "append", "multAll", "getIndex", "addAll", "append", "multAll", "getIndex", "getIndex", "getIndex"]
args = [[], [2], [3], [7], [2], [0], [3], [10], [2], [0], [1], [2]]
expected = [None, None, None, None, None, 10, None, None, None, 26, 34, 20]
test(methods, args, expected)

methods = ["Fancy", "addAll", "append", "multAll", "getIndex"]
args = [[], [3], [7], [2], [0]]
expected = [None, None, None, None, 14]
test(methods, args, expected)

methods = ["Fancy"]
args = [[]]
expected = [None]
test(methods, args, expected)

methods = ["Fancy", "append", "multAll", "multAll", "getIndex", "getIndex"]
args = [[], [1], [2], [3], [0], [0]]
expected = [None, None, None, None, 6, 6]
test(methods, args, expected)

methods = ["Fancy", "append", "multAll", "multAll", "getIndex", "append", "multAll", "multAll", "getIndex"]
args = [[], [1], [2], [3], [0], [1], [2], [3], [1]]
expected = [None, None, None, None, 6, None, None, None, 6]
test(methods, args, expected)

methods = ["Fancy"] + ["append", "addAll", "append", "multAll", "getIndex", "addAll", "append", "multAll", "getIndex", "getIndex"] * 4000
args = [[]] + [[2], [3], [7], [2], [0], [3], [10], [2], [0], [1]] * 4000
test(methods, args)

# LeetCode Submission
# Runtime: 1020 ms, faster than 75.22% of Python3 online submissions for Fancy Sequence.
# Memory Usage: 54.5 MB, less than 61.77% of Python3 online submissions for Fancy Sequence.
# 107 / 107 test cases passed.

# Algorithm

#      m, inc
# a    1,  0
# +2:  1,  2
# *3:  3,  6
#                m, inc
# b    3,  6     1,  0
# +4:  3, 10     1,  4
# *5: 15, 50     5, 20

# Calculation of m and inc for b
# m   = 15 / 3 = 5
# inc = 50 - 6 * 15 = 20
