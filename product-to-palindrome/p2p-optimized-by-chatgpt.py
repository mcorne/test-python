# Optimized by ChatGPT from translated-by-chatgpt.py

import time


class ProductTopPalindrome:

    def __init__(self):
        self.errorMessage = None
        self.iterations = 0
        self.palindrome = None
        self.rangeBegin = None
        self.max_palindrome = 0

    def calculate_palindrome(self, range_end, range_begin=None):
        if range_begin is None:
            range_begin = 1

        range_begin = int(range_begin)
        range_end = int(range_end)

        if not self.is_valid_range(range_end, range_begin):
            return False

        self.rangeBegin = range_begin
        start_time = time.time()

        # Start iterating with the largest products, decrementing the range
        for a in range(range_end, range_begin - 1, -1):
            for b in range(a, range_begin - 1, -1):  # Only check when `b <= a`
                product = a * b
                self.iterations += 1

                # Stop if product is smaller than the largest palindrome found
                if product <= self.max_palindrome:
                    break

                if self.is_palindrome(product):
                    self.max_palindrome = product
                    self.palindrome = {"a": a, "b": b, "p": product}
                    # Early exit: found the largest possible palindrome
                    break

        self.time = round((time.time() - start_time), 3)  # Execution time

        return None

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
            "time": f"{self.time} seconds",
            "error": self.errorMessage,
        }


palindrome = ProductTopPalindrome()
palindrome.calculate_palindrome(9999)

print(palindrome.print_report())
