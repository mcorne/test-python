# https://leetcode.com/problems/print-in-order/
import threading
from time import sleep
from typing import Callable

class Foo:
    def __init__(self):
        self.first_event = threading.Event()
        self.second_event = threading.Event()
        self.methods = [self.first, self.second, self.third]

    def first(self, printFirst: Callable) -> None:
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.first_event.set()

    def second(self, printSecond: Callable) -> None:
        self.first_event.wait()
        # printSecond() outputs "second". Do not change or remove this line.
        printSecond()
        self.second_event.set()

    def third(self, printThird: Callable) -> None:
        self.second_event.wait()
        # printThird() outputs "third". Do not change or remove this line.
        printThird()

class Prints:
    def __init__(self):
        self.methods = [self.printFirst, self.printSecond, self.printThird]
        self.result = ""

    def printFirst(self):
        self.result += "first"

    def printSecond(self):
        self.result += "second"


    def printThird(self):
        self.result += "third"


def test(nums):
    foo = Foo()
    prints = Prints()
    for num in nums:
        num -= 1
        thread = threading.Thread(target=foo.methods[num], args=(prints.methods[num],))
        thread.start()
        if num == 2:
            last_thread = thread
    while last_thread.is_alive():
        sleep(0.1)
    status = "OK" if prints.result == "firstsecondthird" else "ERROR"
    print(status, prints.result)

# Tests
nums = [1,2,3]
test(nums)

nums = [1,3,2]
test(nums)

# LeetCode Submission
# Runtime: 70 ms, faster than 77.61% of Python3 online submissions for Print in Order.
# Memory Usage: 14.4 MB, less than 94.51% of Python3 online submissions for Print in Order.
# 36 / 36 test cases passed.
