class Fancy:
    def __init__(self):
        self.operations = []
        self.values = []

    def addAll(self, inc: int) -> None:
        self.operations.append([inc, "+"])

    def append(self, value: int) -> None:
        self.values.append([value, len(self.operations)])

    def getIndex(self, idx: int) -> int:
        if idx >= len(self.values):
            return -1
        if self.values[idx][1] < len(self.operations):
            self.updateValue(idx)
        return self.values[idx][0] % (10**9 + 7)

    def multAll(self, m: int) -> None:
        self.operations.append([m, "*"])

    def updateValue(self, value_idx: int)-> int:
        value, operation_idx = self.values[value_idx]
        for operand, operator in self.operations[operation_idx:]:
            if operator == "+":
                value += operand
            else:
                value *= operand
        self.values[value_idx] = [value, len(self.operations)]

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
# Error: Time Limit Exceeded with 49002 methods/args at 104th test (OK though when running test alone: 6600 ms)
