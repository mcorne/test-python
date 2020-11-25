class Fancy:
    def __init__(self):
        self.sequence = []

    def append(self, val: int) -> None:
        self.sequence.append(val)

    def addAll(self, inc: int) -> None:
        self.sequence = [val+inc for val in self.sequence]

    def multAll(self, m: int) -> None:
        self.sequence = [val*m for val in self.sequence]

    def getIndex(self, idx: int) -> int:
        if idx >= len(self.sequence):
            return -1
        return self.sequence[idx] % (10**9 + 7)

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
def test(methods, args, expected):
    sequence = Fancy.generateSequence(methods, args)
    status = "OK" if sequence == expected else "ERROR"
    print(status, sequence)

methods = ["Fancy", "append", "addAll", "append", "multAll", "getIndex", "addAll", "append", "multAll", "getIndex", "getIndex", "getIndex"]
args = [[], [2], [3], [7], [2], [0], [3], [10], [2], [0], [1], [2]]
expected = [None, None, None, None, None, 10, None, None, None, 26, 34, 20]
# test(methods, args, expected)

methods = ["Fancy"] + ["append", "addAll", "append", "multAll", "getIndex", "addAll", "append", "multAll", "getIndex", "getIndex"] * 4000
args = [[]] + [[2], [3], [7], [2], [0], [3], [10], [2], [0], [1]] * 4000
expected = [None, None, None, None, None, 10, None, None, None, 26, 34, 20]
test(methods, args, expected)

# LeetCode Submission
# Error: Time Limit Exceeded
