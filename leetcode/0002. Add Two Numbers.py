class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        first = None
        prev = None
        value = 0
        while l1 or l2 or value:
            if l1:
                value += l1.val
                l1 = l1.next
            if l2:
                value += l2.val
                l2 = l2.next
            node = ListNode()
            value, node.val = divmod(value, 10)
            if prev:
                prev.next  = node
            else:
                first = node
            prev = node
        return first

    @classmethod
    def list2nodes(cls, values: list) -> ListNode:
        first = None
        prev = None
        for value in values:
            node = ListNode(value)
            if prev:
                prev.next = node
            else:
                first = node
            prev = node
        return first

    @classmethod
    def nodes2list(cls, node: ListNode) -> list:
        values = []
        while node:
            values.append(node.val)
            node = node.next
        return values


# Tests
s = Solution()

l1 = s.list2nodes([2,4,3])
l2 = s.list2nodes([5,6,4])
res = s.addTwoNumbers(l1, l2)
print(s.nodes2list(res))

l1 = s.list2nodes([0])
l2 = s.list2nodes([0])
res = s.addTwoNumbers(l1, l2)
print(s.nodes2list(res))

l1 = s.list2nodes([9,9,9,9,9,9,9])
l2 = s.list2nodes([9,9,9,9])
res = s.addTwoNumbers(l1, l2)
print(s.nodes2list(res))

# LeetCode Submission
# Runtime: 64 ms, faster than 91.46% of Python3 online submissions for Add Two Numbers.
# Memory Usage: 14.2 MB, less than 100.00% of Python3 online submissions for Add Two Numbers.
# 1568 / 1568 test cases passed.