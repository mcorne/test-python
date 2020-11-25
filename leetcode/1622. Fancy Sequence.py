class Fancy:
    def __init__(self):
        self.actions = []
        self.index = 0
        self.values = []

    def append(self, val: int) -> None:
        self.values.append([self.index, val])
        self.index += 1

    def addAll(self, inc: int) -> None:
        self.actions.append([self.index, inc, "+"])
        self.index += 1

    def multAll(self, m: int) -> None:
        self.actions.append([self.index, m, "*"])
        self.index += 1

    def getIndex(self, idx: int) -> int:
        if idx >= len(self.values):
            return -1
        val = self.updateValue(idx)
        return val % (10**9 + 7)

    def updateValue(self, idx):
        val_idx, val = self.values[idx]
        if val_idx < self.index:
            for action_idx, val_op, op in self.actions:
                if action_idx > val_idx:
                    if op == "+":
                        val += val_op
                    else: # *
                        val *= val_op
            self.values[idx] = [self.index-1, val]
        return val

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

methods = ["Fancy"] + ["append", "addAll", "append", "multAll", "getIndex", "addAll", "append", "multAll", "getIndex", "getIndex"] * 4000
args = [[]] + [[2], [3], [7], [2], [0], [3], [10], [2], [0], [1]] * 4000
test(methods, args)

# LeetCode Submission
# Error: Time Limit Exceeded with 49003 methods/args (OK though when running test alone: 8512 ms)
