# https://leetcode.com/problems/fizz-buzz-multithreaded/
import threading
from time import sleep
from typing import Callable


class FizzBuzz:
    def __init__(self, n: int):
        self.event = threading.Event()
        self.i = 1
        self.n = n
        self.methods = [self.fizz, self.buzz, self.fizzbuzz, self.number]

    # printFizz() outputs "fizz"
    def fizz(self, printFizz: Callable) -> None:
        while self.i <= self.n:
            if not (self.i % 3) and self.i % 5:
                printFizz()
                self.i += 1
                self.event.set()
            self.event.wait()

    # printBuzz() outputs "buzz"
    def buzz(self, printBuzz: Callable) -> None:
        while self.i <= self.n:
            if self.i % 3 and not (self.i % 5):
                printBuzz()
                self.i += 1
                self.event.set()
            self.event.wait()

    # printFizzBuzz() outputs "fizzbuzz"
    def fizzbuzz(self, printFizzBuzz: Callable) -> None:
        while self.i <= self.n:
            if not (self.i % 3) and not (self.i % 5):
                printFizzBuzz()
                self.i += 1
                self.event.set()
            self.event.wait()

    # printNumber(x) outputs "x", where x is an integer.
    def number(self, printNumber: Callable) -> None:
        while self.i <= self.n:
            if self.i % 3 and self.i % 5:
                printNumber(self.i)
                self.i += 1
                self.event.set()
            self.event.wait()


class Prints:
    def __init__(self):
        self.methods = [
            self.printFizz,
            self.printBuzz,
            self.printFizzBuzz,
            self.printNumber,
        ]
        self.result = []

    def printFizz(self):
        self.result.append("fizz")

    def printBuzz(self):
        self.result.append("buzz")

    def printFizzBuzz(self):
        self.result.append("fizzbuzz")

    def printNumber(self, int):
        self.result.append(int)


def test(n, expected):
    fizzbuzz = FizzBuzz(n)
    prints = Prints()
    for i, target in enumerate(fizzbuzz.methods):
        thread = threading.Thread(target=target, args=(prints.methods[i],))
        thread.start()
    while fizzbuzz.i <= n:
        sleep(0.1)
    status = "OK" if prints.result == expected else "ERROR"
    print(status, prints.result)


# Tests
n = 15
expected = [
    1,
    2,
    "fizz",
    4,
    "buzz",
    "fizz",
    7,
    8,
    "fizz",
    "buzz",
    11,
    "fizz",
    13,
    14,
    "fizzbuzz",
]
test(n, expected)

n = 5
expected = [1, 2, "fizz", 4, "buzz"]
test(n, expected)

# LeetCode Submission
# Runtime: 148 ms, faster than 12.28% of Python3 online submissions for Fizz Buzz Multithreaded.
# Memory Usage: 14.5 MB, less than 62.11% of Python3 online submissions for Fizz Buzz Multithreaded.
# 9 / 9 test cases passed.
