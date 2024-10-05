# Translated by ChatGPT from original.php

import time


class ProductTopPalindrome:

    def __init__(self):
        self.candidates = []  # Reverse sorted by product, factor => product
        self.errorMessage = None
        self.iterations = 0
        self.palindrome = None
        self.rangeBegin = None
        self.time = None

    def calculate_palindrome(self, range_end, range_begin=None):
        if range_begin is None:
            range_begin = 1

        range_begin = int(range_begin)
        range_end = int(range_end)

        if not self.is_valid_range(range_end, range_begin):
            return False

        product = range_end * range_end

        if not isinstance(product, int):
            self.errorMessage = (
                f"The product {range_end} * {range_end} is too large for this machine."
            )
            return False

        self.insert_candidate({"a": range_end, "b": range_end, "p": product})

        self.rangeBegin = range_begin
        self.time = time.time()

        while True:
            candidate = self.get_next_candidate()
            if candidate is None:
                break

            self.iterations += 1

            if self.is_palindrome(candidate["p"]):
                self.palindrome = candidate
                break

        self.time = round((time.time() - self.time), 3)

        return None

    def get_next_candidate(self):
        if not self.candidates:
            return None

        candidate = self.candidates.pop(0)
        next_factor_a = candidate["a"] - 1

        if candidate["b"] == next_factor_a and next_factor_a >= self.rangeBegin:
            self.insert_candidate(
                {
                    "a": next_factor_a,
                    "b": next_factor_a,
                    "p": next_factor_a * next_factor_a,
                }
            )

        next_factor_b = candidate["b"] - 1
        product = candidate["p"] - candidate["a"]

        if product >= candidate["a"] and next_factor_b >= self.rangeBegin:
            self.insert_candidate(
                {"a": candidate["a"], "b": next_factor_b, "p": product}
            )

        return candidate

    def insert_candidate(self, new_candidate):
        candidates = []

        for candidate in self.candidates:
            if new_candidate and (
                new_candidate["p"] > candidate["p"]
                or (
                    new_candidate["p"] == candidate["p"]
                    and new_candidate["a"] > candidate["a"]
                )
            ):
                candidates.append(new_candidate)
                new_candidate = None  # Mark new candidate as inserted

            candidates.append(candidate)

        if new_candidate:
            candidates.append(new_candidate)

        self.candidates = candidates

    def is_palindrome(self, number):
        number = str(number)
        return number == number[::-1]

    def is_valid_range(self, range_end, range_begin):
        if range_end < 0:
            self.errorMessage = (
                "The end of the range must be a positive non-null integer."
            )
            return False

        if range_begin < 0 or range_begin > range_end:
            self.errorMessage = f"The beginning of the range must be a positive non-null integer, lower than {range_end}"
            return False

        return True

    def print_candidate(self, candidate):
        return f"{candidate['a']} * {candidate['b']} = {candidate['p']}"

    def print_report(self):
        return {
            "palindrome": (
                self.print_candidate(self.palindrome) if self.palindrome else "none"
            ),
            "iterations": self.iterations,
            "time": self.time,
            "stack": [self.print_candidate(candidate) for candidate in self.candidates],
            "error": self.errorMessage,
        }


palindrome = ProductTopPalindrome()
palindrome.calculate_palindrome(9999)

print(palindrome.print_report())
