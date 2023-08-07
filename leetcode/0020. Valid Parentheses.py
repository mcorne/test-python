class Solution:
    def isValid(self, s: str) -> bool:
        closing = ""
        for c in s:
            if c == "(":
                closing += ")"
            elif c == "[":
                closing += "]"
            elif c == "{":
                closing += "}"
            elif closing and closing[-1] == c:
                closing = closing[0:-1]
            else:
                return False
        return not closing


# Tests
def test(s, expected):
    solution = Solution()
    is_valid = solution.isValid(s)
    status = "OK" if is_valid == expected else "ERROR"
    print(status, is_valid)


# Tests
s = "()"
expected = True
test(s, expected)

# Tests
s = "()[]{}"
expected = True
test(s, expected)

# Tests
s = "(]"
expected = False
test(s, expected)

# Tests
s = "((("
expected = False
test(s, expected)

# Tests
s = ")))"
expected = False
test(s, expected)

# Tests
s = "(([{}[]][]))()"
expected = True
test(s, expected)

# LeetCode Submission
# Runtime 38ms Beats 88.94% of users with Python3
# Memory 16.15mb Beats 99.09% of users with Python3
